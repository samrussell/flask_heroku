from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  things = [
          { 'type' : 'food', 'name' : 'banana' },
          { 'type' : 'food', 'name' : 'tofu' },
          { 'type' : 'bike', 'name' : 'suzuki' },
          ]
  return render_template('hello.html', things=things)

