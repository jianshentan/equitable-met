import os
import sys
import random
from flask import (
    g, Blueprint, render_template, jsonify, request, 
    redirect, url_for
)
from .forms import SubscribeForm
from .mailchimp import mc

bp = Blueprint('main', __name__)

@bp.route('/')
def main():
    return render_template('index.html')

@bp.route('/subscribe', methods=['POST'])
def subscribe():
    '''
    Validate subscribe form and add subscriber
    Returns a json formatted:
    {
        success: <bool>,
        errors: <str> (error to display)
    }
    '''
    form = SubscribeForm(request.form, csrf_enabled=False)
    if form.validate():
        mc.add_or_update_user(form.email.data)
        return jsonify(success=True)
    else:
        return jsonify(success=False, errors=form.errors["email"][0])
