import os

from dotenv import load_dotenv
from flask import Flask

from logic import index, report
from validators import escape


def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    ip_or_domain = os.environ.get("IP_OR_DOMAIN")
    port = os.environ.get("PORT")
    print(f"IP_OR_DOMAIN: {ip_or_domain}, PORT: {port}")  # Для перевірки значень
    
    app.config["IP_OR_DOMAIN_WITH_PORT"] = "{}:{}".format(ip_or_domain, port)
    print(f"IP_OR_DOMAIN_WITH_PORT: {app.config['IP_OR_DOMAIN_WITH_PORT']}")  # Для перевірки результату
    
    app.config["CAPTCHA_TOKEN"] = os.getenv("CAPTCHA_TOKEN")
    app.config["CAPTCHA_SITE_KEY"] = os.getenv("CAPTCHA_SITE_KEY")
    
    print(f"CAPTCHA_TOKEN: {app.config['CAPTCHA_TOKEN']}, CAPTCHA_SITE_KEY: {app.config['CAPTCHA_SITE_KEY']}")  # Для перевірки токенів

    from jobs import rq
    rq.init_app(app)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/report', 'report', report, methods=["GET", "POST"])
    app.add_template_filter(escape, "e")

    return app
