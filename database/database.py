import os.path
from flask_sqlalchemy import SQLAlchemy
from .data import titles, messages, news_posts, projects, skills, web_software
db = SQLAlchemy()

# Define models
class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    text = db.Column(db.String(255))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_name = db.Column(db.String(50), db.ForeignKey('title.name'))
    content = db.Column(db.String(255))

class NewsPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    image = db.Column(db.String(255))
    description = db.Column(db.String(255))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    image = db.Column(db.String(255))
    description = db.Column(db.String(255))

class WebSoftware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    image = db.Column(db.String(255))
    description = db.Column(db.String(255))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    name = db.Column(db.String(50))
    level = db.Column(db.Integer)
    experience = db.Column(db.String(50))

def database_setup(app):
    db_file_path = 'portfolio.db'
    if not os.path.exists(db_file_path):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
        db.init_app(app)
        with app.app_context():
            db.create_all()
            load_data()
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
        db.init_app(app)

def load_data():
    # Load data only if needed
    if not Title.query.all():
        # Load titles
        for name, text in titles.items():
            title = Title(name=name, text=text)
            db.session.add(title)

        # Load messages
        for name, content in messages.items():
            title = Title.query.filter_by(name=name).first()
            if title:
                for msg in content:
                    message = Message(title_name=name, content=msg)
                    db.session.add(message)

        # Load news posts
        for post_data in news_posts:
            post = NewsPost(title=post_data[0], link=post_data[1], image=post_data[2], description=post_data[3])
            db.session.add(post)

        # Load projects
        for project_data in projects:
            project = Project(name=project_data[0], link=project_data[1], image=project_data[2], description=project_data[3])
            db.session.add(project)

        for web_data in web_software:
            web_software_instance = WebSoftware(name=web_data[0], link=web_data[1], image=web_data[2], description=web_data[3])
            db.session.add(web_software_instance)

        # Load skills
        for category, skills_list in skills:
            for skill_data in skills_list:
                skill = Skill(category=category, name=skill_data[0], level=skill_data[1], experience=skill_data[2])
                db.session.add(skill)

        # Commit changes
        db.session.commit()


def get_messages():
    return {title.name: [msg.content for msg in Message.query.filter_by(title_name=title.name).all()] for title in Title.query.all()}

def get_titles():
    return {title.name: title.text for title in Title.query.all()}

def get_news_posts():
    return [[post.title, post.link, post.image, post.description] for post in NewsPost.query.all()]

def get_projects():
    return [[project.name, project.link, project.image, project.description] for project in Project.query.all()]

def get_web_software():
    return [[web_software.name, web_software.link, web_software.image, web_software.description] for web_software in WebSoftware.query.all()]

def get_skills():
    return [[skill[0], [[s[0], s[1], s[2]] for s in skill[1]]] for skill in skills]