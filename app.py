#import package
from flask import Flask

#Creating flask application
app = Flask(__name__)

#Home page that users will see first
@app.route('/')
def home():
    return 'Hello world!'
#About page
@app.route('/about')
def about():
    return 'About us!'

#Contact us page
@app.route('/contact_us')
def contact_us():
    return 'You can contact us through email: "random@gmail.com'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

