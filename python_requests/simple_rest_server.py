# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')


# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case

@app.route('/signup/', methods=['POST'])
def signup():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)

@app.route('/tweets/', methods=['POST'])
def simple_api():
    key =request.form["apikey"]
    secret =request.form["secret"]
    result = dict()
    result['APIKEY']=key
    result['SECRET'] = secret
    return flask.jsonify(**result)




# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("9080")
  )
