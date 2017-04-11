from home import db

class User(db.Model):
	username = db.Column(db.String(80))
	password = db.Column(db.String(16))
        
        def __init__(self, username, password):
                self.username = username
                self.password = password

        def user_name_exists(username):
                exists = Session.query(exists().where(User.username == username)).scalar()
                return exists
