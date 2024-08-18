This repository contains a Flask-based website showcasing my web_software engineering skills and projects. The website features various sections, including a background section, project showcases, news posts, and information about web applications and games I've developed.

Site Functionality:

1. Home Page (/welcome.html): The main landing page displays a featured project and a featured news post, along with links to explore more content.

2. Background (/background.html): This section provides an overview of my journey as a web_software engineer, highlighting key milestones and achievements throughout the years. It also showcases my skill levels across different programming languages and technologies, represented by progress bars. Hover over the bars to see more details about each skill.

3. Project Showcase (/showcase.html): Here, you can find detailed information about my web_software engineering projects, including descriptions, images, and links to the respective GitHub repositories. The projects are divided into two categories: general projects and web applications/dashboards.

4. Web Applications and Dashboards (/web_software.html): This section displays only the web application and dashboard projects I've developed, demonstrating my expertise in web development technologies such as Flask, Bootstrap, and various frameworks.

5. News (/news.html): In this section, I share articles and insights related to technology, web_software development, game design, and coding tutorials. Each news post includes a title, image, description, and a link to the full article.

6. Navigation (/clean_design.html): The website features a responsive navigation bar at the top, allowing easy access to all sections. The navigation bar also includes links to my GitHub and LinkedIn profiles.

7. Animation (/static/javascript/): The website incorporates subtle animations using the anime.js library. Elements such as titles, images, and navigation links are animated when the page loads, creating a smooth and engaging user experience.

Installation and Setup:

1. Ensure you have Python installed on your system.

2. Clone the repository to your local machine.

3. Install the required dependencies by running the following command in your terminal or command prompt:

   ```
   pip install -r requirements.txt
   ```
   OR

   If you prefer to manually install libraries, you can do the following commands in your terminal:

   ```
   pip install Flask==3.0.
   pip install flask_sqlalchemy
   ```

4. To set up the database, run the following command:

   ```
   python main.py
   ```

   This will create a `portfolio.db` file in the `instance` directory if it doesn't already exist.

5. To run the website locally, execute the following command:

   ```
   python main.py
   ```

   The website should now be accessible at `http://localhost:5000`.

Please note that the database (`instance/portfolio.db`) is initially empty. Any changes made to the data during runtime will be reflected in the database file. To reset the database to its initial state, simply delete the `instance/portfolio.db` file, and it will be recreated with the default data upon the next run.

The website is designed to showcase my skills and projects as a web_software engineering student. Feel free to explore the different sections and explore the functionality. If you have any questions or need further assistance, please don't hesitate to reach out.