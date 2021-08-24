from flask import redirect, url_for, render_template, session, request
from app.main import bp
from app.main.forms import LandingPageForm
import json

#################
#    Routes     #
#################

@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = LandingPageForm()
    # send data from form to be processed by the concat function on submit
    if form.validate_on_submit() or request.method == 'POST':
        session['word_one'], session['word_two'] = form.word_one.data, form.word_two.data
        return redirect(url_for('functions.concat'))
    return render_template('main/index.html', form=form)

@bp.route('/health_check', methods=['GET'])
def health_check():
    return json.dumps({'alive': True}), 200, {'ContentType': 'application/json'}
