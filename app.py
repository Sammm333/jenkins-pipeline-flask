from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# This is a simple Flask application that can be used to demonstrate Jenkins CI/CD pipeline.
# It listens on all interfaces (