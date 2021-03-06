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
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            Rotate by: <input name="rot" type="text" value="0">
            <textarea name="text">{}</textarea>
            <input type="submit" value="submit">
        </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form["rot"]
    rotation = int(rotation)
    unencrypted = request.form["text"]
    rotated = rotate_string(unencrypted,rotation)
    return form.format(rotated)
@app.route("/")
def index():
    return form.format('')

app.run()