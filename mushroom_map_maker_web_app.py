'''
~~~~~~~~~~~

Mushroom_map_maker_web_app

A flask app that uses the mushroom_map_maker module to ask a user for the genus and species of a mushroom.
This data is used to render a heatmap of that mushroom's distribution across the globe using data from
mushroomobserver.org.
'''

from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for
from forms import UserInput
import mushroom_map_maker

'''Creates an instance of the Flask class as the object 'app', configures the flask object 'app',
and passes 'app' to the Bootstrap class.'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)

'''All the routes.
'''

@app.route('/')
def index():
    return render_template('index.html', page='home') # you can pass variables to use in templates

@app.route('/user_input', methods=['GET', 'POST'])
def user_input():
    form = UserInput()
    if form.validate_on_submit():
        genus_name = form.genus_name.data.strip(' ')
        species_name = form.species_name.data.strip(' ')
        return redirect(url_for('result', genus_name=genus_name, species_name=species_name))
    return render_template('user_input.html', form=form, page='search')

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
