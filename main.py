from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

#Define route for the homepage
@app.route('/')
def home():
    posts = []
    for file in os.listdir('posts'):
        if file.endswith('.md'):
            title = file[:-3]
            posts.append(title)
    return render_template('index.html', posts=posts)

# Define the route to handle individual blog posts
@app.route('/posts/<path:path>')
def posts(path):
    with open(f'posts/{path}.md', 'r') as file:
        content = file.read()
        html = markdown.markdown(content)
    # Render the post template with the title and HTML content
    return render_template('post.html', title=path.capitalize(), content=html)
# Check if the script is run directly and starts the app if so
if __name__ =='__main__':
    app.run(debug=True)    
