import os
from dotenv import load_dotenv

# config files will generally parse the environment or a .env (or config file)
# and create a config object which is then loaded by main to create settings for
# your app. This one obviously doesnt do much because, well, it doesn't need to.

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hey-bitch-boy'
