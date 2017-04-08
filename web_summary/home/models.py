from werkzeug import generate_password_hash, check_password_hash
from home import db

class User(db.Model):

	def __repr__(self):
		return '<User %r>' % (self.user_name)

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(16), nullable=False)
	last_name = db.Column(db.String(16), nullable=False)
	user_name = db.Column(db.String(16),  index = True, unique = True, nullable=False)
	email = db.Column(db.String(60), index = True, unique = True, nullable=False)

	_password = db.Column('password', db.String(16))

	def _get_password(self):
		return self._password

	def _set_password(self, password):
		self._password = generate_password_hash(password)

	password = db.synonym('_password', descriptor=property(_get_password, _set_password))

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	@classmethod
	def authenticate(cls, user_name, password):
		user = User.query.filter(db.or_(User.user_name == user_name)).first()

		if user:
			authenticated = user.check_password(password)
		else:
			authenticated = False
		return user, authenticated

	@classmethod
	def is_user_name_taken(cls, user_name):
		return db.session.query(db.exists().where(User.user_name==user_name)).scalar()

	@classmethod
	def is_email_taken(cls, email_address):
		return db.session.query(db.exists().where(User.email==email_address)).scalar()