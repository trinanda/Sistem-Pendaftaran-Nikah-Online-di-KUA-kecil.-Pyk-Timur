DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://uci:12345@service_postgresql_on_docker/nikah_online'
DATABASE_FILE = SQLALCHEMY_DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = '12345'

#############################################################################################################
# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

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

#############################################################################################################
PDF_FOLDER = 'web_app/files/pdf/'
TEMPLATE_FOLDER = 'web_app/templates/'
#############################################################################################################