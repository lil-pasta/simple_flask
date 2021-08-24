from flask import render_template, request, session, redirect, url_for
from app.functions import bp

##########
# Routes #
##########
@bp.route('/concat', methods=['GET', 'POST'])
def concat():
    if 'word_one' in session and 'word_two' in session:
        word = f"{session['word_one']}{session['word_two']}"
        return render_template('functions/concat.html', word=word)
    else:
        abort(404)
