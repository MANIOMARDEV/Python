# server.py file

# Import all the controllers
from flask_app.controllers import authors, books
# Import the app
from flask_app import app

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for windows
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
