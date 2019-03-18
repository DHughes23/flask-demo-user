"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import P_Form
from app.models import Profile
from werkzeug.security import check_password_hash
import datetime
from werkzeug.utils import secure_filename
import os, random

###
# Routing for your application.
###



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = P_Form()
    
    if request.method == 'POST' and form.validate_on_submit():
        f_name = form.f_name.data
        l_name = form.l_name.data
        gender = form.gender.data
        e_address = form.e_address.data
        location = form.location.data
        bio = form.biography.data
        
        photo = request.files['photo']
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        userID = createID(f_name, l_name)
        date_created = date_joined()
        
        profile = Profile(userID = userID, f_name = f_name, l_name = l_name, gender = gender, e_address = e_address, location = location, biography = bio, date = date_created, photo = filename)        
        db.session.add(profile)
        db.session.commit()
        
        '''db = app.connect_db()
        cur = db.cursor()
        cur.execute('insert into users (name, email) values (%s, %s)', (request.form['name'], request.form['email']))
        db.commit()'''
        
        flash('Your profile was successfully added.', 'success')
        return redirect(url_for('home'))
        
    flash_errors(form)
    return render_template('profile.html', form = form)

@app.route('/profiles')
def profiles():
    db = app.connect_db()
    cur = db.cursor()
    users = Profile.query.all()
    return render_template('profiles.html', users=users)

@app.route('/profiles/<userId>')
def userProfile(userId):
    """Render the website's about page."""
    user = Profile.query.get(userId)
    return render_template('userProfile.html', user=user)

def createID(f_name, l_name):
    f = f_name[0]
    l = l_name[0]
    id = f.upper()+l.upper()+str(random.randint(0,1000))
    return id
    
def date_joined():
    date = datetime.date.today().strftime("%B %d, %Y")
    return "Joined " + date



# Flash errors from the form if validation fails with Flask-WTF
# http://flask.pocoo.org/snippets/12/
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
