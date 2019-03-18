from . import db

class Profile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'user_profiles'
    
    userID = db.Column(db.String, primary_key=True)
    f_name = db.Column(db.String(80))
    l_name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    e_address = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(255))
    biography = db.Column(db.String(1000))
    date = db.Column(db.String(20))
    photo = db.Column(db.String(30))


    '''def __init__(self, userID, f_name, l_name, gender, e_address, location, biography, date, photo):
        self.userID = userID
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.e_address = e_address
        self.location = location
        self.biography = biography
        self.date = date
        self.photo = photo'''


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username
