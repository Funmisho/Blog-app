# Blog App

A simple blog application built with Flask that serves Markdown posts as HTML pages. This project demonstrates basic Flask routing, template rendering, and Markdown integration.

## Features

- Displays a list of blog posts on the home page
- Renders individual blog posts from Markdown files
- Basic HTML templating with Jinja2
- Supports headings, bold text, and other Markdown formatting

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Flask and Markdown libraries

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Funmisho/Blog-app.git
   cd Blog-app

Install the required packages:

bash
Copy code
pip install flask markdown
Project Structure
plaintext
Copy code
.
├── main.py                # Main application file
├── templates/             # HTML templates
│   ├── index.html         # Home page template
│   └── post.html          # Individual post template
├── posts/                 # Folder containing Markdown files for blog posts
│   └── hello.md           # Example blog post
└── README.md              # This README file
Adding Blog Posts
Add Markdown files to the posts/ directory. Each Markdown file should have a .md extension. For example:

markdown
Copy code
# Title of the Post

This is the content of the post written in Markdown format.
Running the Application
Start the Flask development server:

bash
Copy code
python3 main.py
Open your web browser and go to http://127.0.0.1:5000 to view the app.

Deployment
To deploy this application for public access, consider using platforms like Heroku or Render. Follow their documentation for Flask app deployment.

Usage
Homepage: Lists all available blog posts by title.
Individual Post: Click on a title to view the blog post content rendered from Markdown.
License
This project is licensed under the MIT License.

sql
Copy code

Just copy and paste this into your `README.md` file! Let me know if you need any more help with it.
