from flask import Flask
from flask_assets import Environment, Bundle
from flask_basicauth import BasicAuth
from datetime import datetime
from hashlib import md5
from .routes import bp
from .mailchimp import mc
import secrets

def create_app(
        package_name=__name__, 
        static_folder='static',
        template_folder='templates',
        **config_overrides):
                
    static_url_path = '/assets'        

    # initialize app
    app = Flask(package_name,
                static_url_path=static_url_path,
                static_folder=static_folder,
                template_folder=template_folder)

    # Apply overrides
    app.config.update(config_overrides)
    
    # set auth
    # app.config['BASIC_AUTH_FORCE'] = True
    # app.config['BASIC_AUTH_USERNAME'] = secrets.BASIC_AUTH_USERNAME
    # app.config['BASIC_AUTH_PASSWORD'] = secrets.BASIC_AUTH_PASSWORD
    # basic_auth = BasicAuth(app)
    
    # set mailchimp settings 
    mc_user = secrets.MAILCHIMP_USERNAME
    mc_key = secrets.MAILCHIMP_KEY
    mc_list_id = secrets.MAILCHIMP_LIST_ID
    
    # load mailchimp credentials
    mc.set_credentials(mc_user, mc_key)
    mc.set_list_id(mc_list_id)
    
    # TODO: HACK
    app.debug = secrets.DEBUG

    # TODO this needs work, but works as a stop-gap
    if app.debug:
        # Set up webassets so that they are precompiled for deployment
        assets = Environment(app)

        css = Bundle('css/*.sass',
                     #filters='sass,cssmin',
                     filters='sass',
                     depends=[
                       'css/*.sass',
                       'css/**/*.sass',
                       'css/**/**/*.sass'
                     ],
                     output='gen/style.css')

        js = Bundle('js/*.js',
                    #filters='jsmin',
                    depends=[
                        'js/*.js',
                        'js/**/*.js',
                        'js/**/**/*.js'
                    ],
                    output='gen/main.js')

        assets.register('css_all', css)
        assets.register('js_all', js)

        app.config['JS_URLS'] = assets['js_all'].urls
        app.config['CSS_URLS'] = assets['css_all'].urls
    else:
        hash = md5(datetime.utcnow().isoformat().encode('utf8')).hexdigest()[:10]
        app.config['JS_URLS'] = lambda: ['{}/js/gen/main.js?{}'.format(static_url_path, hash)]
        app.config['CSS_URLS'] = lambda: ['{}/css/gen/style.css?{}'.format(static_url_path, hash)]

    # Register Routes in routes.py
    app.register_blueprint(bp)

    return app

