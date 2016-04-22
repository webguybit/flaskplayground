# Create dummy secret key so we can use sessions
SECRET_KEY = '123490'

# Create in-memory database
DATABASE_FILE = 'tbl_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
#SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
#SECURITY_PASSWORD_SALT = "ATGUOHAELKiubaq3fgo8hiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False