from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540 px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width:540px;
                height:120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here -->

        <form method="POST">
            <label><strong>Rotate by: </strong>
            <input type="text" name="rot" value="0" />
            </label>
            <textarea name="text"></textarea>
            <input type="submit" Submit Query />
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    # stored values of request parameters, converting types as necessary
    number = int('')
    text = ''
    #encrypt the value of the text parameter using rotate_string


    return '<h1>' + encrypted_string + ' </h1>'

app.route("/")

app.run()