from flask import render_template
from app.errors import bp

#########################
# Custom Error Handlers #
#########################
#
# while not strictly necessary I wanted to give you some examples of how
# custom errors can be written and served in a flask application

@bp.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@bp.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(413)
def too_large(error):
    return render_template('errors/413.html'), 413

