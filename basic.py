from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     DateTimeField, RadioField, SelectField, TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'youcantguess!'


class InforForm(FlaskForm):
    breed = StringField('Enter Breed', validators=[DataRequired()])
    neutered = BooleanField('Neutered?')
    mood = RadioField('Choose Mood', choices=[
                      ('mood1', 'Happy'), ('mood2', 'excited')])
    food_choice = SelectField(
        u'Pick fav food:', choices=[('chi', 'chicken'), ('bf', 'beef'), ('fs', 'fish')])
    feedback = TextAreaField()

    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():

    form = InforForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['food'] = form.food_choice.data
        session['mood'] = form.mood.data
        session['feedback'] = form.feedback.data

        flash('You Submitted the data')

        return redirect(url_for('thankyou'))
    # flash('Check details again')

    return render_template('home.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5055,  debug=True)
