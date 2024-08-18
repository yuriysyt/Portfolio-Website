from flask import Flask, render_template
from database import database

app = Flask(__name__)

# Initialize the database and load data
database.database_setup(app)

@app.route('/welcome')
@app.route('/')
def welcome():
    title_text = database.get_messages()['welcome']
    title = database.get_titles()['welcome']
    news = database.get_news_posts()
    projects = database.get_projects()

    return render_template('welcome.html',
                           title_text=title_text,
                           title=title,
                           id="welcome",
                           news=news,
                           project=projects)

@app.route('/background')
def background():
    # Get data using functions from setup.py
    title_text = database.get_messages()['background']
    title = database.get_titles()['background']
    skills = database.get_skills()

    # Render the template with data
    return render_template('/background.html',
                            title_text=title_text,
                            skills=skills,
                            title=title,
                            id="background"
                          )

@app.route('/showcase')
def showcase():
    # Get data using functions from setup.py
    title_text = database.get_messages()['showcase']
    title = database.get_titles()['showcase']
    projects = database.get_projects()

    # Render the template with  data
    return render_template('/showcase.html',
                            title_text=title_text,
                            title=title,
                            id="showcase",
                            projects=projects
                          )

@app.route('/web_software')
def dashboards():
    # Get data using functions from setup.py
    title_text = database.get_messages()['web_software']
    title = database.get_titles()['web_software']
    web_software_projects = database.get_web_software()

    # Render the template with data
    return render_template('/web_software.html',
                            title_text=title_text,
                            title=title,
                            id="showcase",
                            projects=web_software_projects
                          )

@app.route('/news')
def news():
    # Get data using functions from setup.py
    title_text = database.get_messages()['news']
    title = database.get_titles()['news']
    news_posts = database.get_news_posts()

    # Render the template with data
    return render_template('/news.html',
                            title_text=title_text,
                            title=title,
                            id="showcase",
                            newss=news_posts
                          )

if __name__ == '__main__':
    app.run()
