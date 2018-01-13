from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for
from forms import UserInput
import mushroom_map_maker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    if form.validate_on_submit():
        genus_name = form.genus_name.data.strip(' ')
        species_name = form.species_name.data.strip(' ')
        return redirect(url_for('result', genus_name=genus_name, species_name=species_name))
    return render_template('user_input.html', form=form)

@app.route('/result/<genus_name>/<species_name>')
def result(genus_name, species_name):
    get_map = mushroom_map_maker.run(genus_name=genus_name,species_name=species_name)
    if get_map == 'mushroom_name_error':
        return render_template('mushroom_name_error.html')
    elif get_map == 'connection_error':
        return render_template('connection_error.html')
    else:
        return render_template('mushroom_map.html')

if __name__ == '__main__':
    app.run(debug=True)

