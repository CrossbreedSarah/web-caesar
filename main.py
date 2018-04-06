from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540 px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width:540px;
                height:120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->

        <form action= "/add" method="POST">
            <label>
            <strong> Rotate by: </strong>
            <input type="text" name="rot" value="0" />
            </label>
            <textarea name="text">{0}</textarea>
            <input type="submit" Value="Submit Query"/>
        </form>
    </body>
</html>

"""

@app.route("/add")
def index():
    return form.format("")

@app.route("/add", methods=['POST'])
def encrypt():

    rot = request.form['rot']
    text = request.form['text']

    new_rotated_string = rotate_string(text, int(rot))   
    return form.format(new_rotated_string)

app.run()