import os, logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from config import Config
from flask import Flask, request, current_app

###############
# App Factory #
###############

# a simple implementation of an app factory pattern. you create your
# blueprints as individual modules and then import and register them
# with the app here. This allows for a more modular app.
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.functions import bp as functions_bp
    app.register_blueprint(functions_bp)

    # logging writes to app.log file when you're not
    # running in debug mode
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', \
                                           maxBytes=10240, \
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('Showsky Startup')
    return app
