

from flask import render_template, session, redirect, url_for, flash
from routes import app


@app.app_errorhandler(403)
def forbidden(err):
    return render_template('403.html'), 403


@app.app_errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.app_errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500

