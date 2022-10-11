from flask import Flask, render_template
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '300922'


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = PhotoForm()
    f = 'static/Images/download.jpeg'
    filename = secure_filename(f.filename)
    f.save(os.path.join(
        app.instance_path, 'static/Images', filename
    ))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
