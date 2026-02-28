from flask import Flask, render_template

# Create the application instance
app = Flask(__name__)

# Create a route. This tells Flask what to do when 
# a user goes to the homepage ('/').
@app.route('/')
def home():
    # render_template looks in the 'templates' folder automatically
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you change code
    app.run(debug=True)
