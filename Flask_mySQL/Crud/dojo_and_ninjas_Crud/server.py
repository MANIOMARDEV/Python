# server.py file

# Import all the controllers
from flask_app.controllers import dojos, ninjas
# Import the app
from flask_app import app

# Ensure file is run directly and not from different
# module, and run localhost on port 5000 for windows
if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)
