import os


ADMIN_PASSWORD = '111'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG=False
SECRET_KEY = 'secret_password'
SITE_WIDTH = 800

#EMAIL SETTINGS
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT=465,
MAIL_USE_SSL=True,
MAIL_USERNAME = 'your_mail@google.com',
MAIL_PASSWORD = 'GooglePasswordHere',
