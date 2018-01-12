from flask import Flask, render_template, redirect, url_for
from forms import UserInput
import mushroom_map_maker


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return 'Home'

@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    if form.validate_on_submit():
        genus_name = form.genus_name.data
        species_name = form.species_name.data
        return redirect(url_for('result', genus_name=genus_name, species_name=species_name))
    return render_template('user_input.html', form=form)

@app.route('/result/<genus_name>/<species_name>')
def result(genus_name, species_name):
    mushroom_map_maker.run(genus_name=genus_name,species_name=species_name)
    return render_template('mushroom_map.html')


if __name__ == '__main__':
    app.run(debug=True)

