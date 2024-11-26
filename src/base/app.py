import os
from flask import Flask, render_template

def create_app():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    
    robots_txt_path = os.path.join(parent_dir, 'robots.txt')
    app = Flask(__name__, static_folder=os.path.join(parent_dir, 'static'), template_folder=os.path.join(parent_dir, 'templates'))

    @app.route("/")
    def dashboard():
        apps = [
            {"name": "ArgoCD", "url": "https://argocd.dev.itlusions.nl/", "logo": "https://argocd.dev.itlusions.nl/assets/images/argo_o.svg"},
            {"name": "Gitea", "url": "https://git.dev.itlusions.nl/", "logo": "https://git.dev.itlusions.nl/assets/img/logo.svg"},
            {"name": "Github", "url": "https://github.com/ITlusions/", "logo": "/static/img/github_logo.webp", "logo_black": "/static/img/github_logo.png"},
            {"name": "Longhorn", "url": "https://longhorn.dev.itlusions.com/", "logo": "https://ranchergovernment.com/hs-fs/hubfs/Longhorn%201.png?width=389&height=319&name=Longhorn%201.png", "logo_black": "/static/img/longhorn-dark.png"},
            {"name": "Grafana", "url": "https://grafana.dev.itlusions.com/", "logo": "/static/img/grafana-icon.svg"},
            {"name": "Prometheus", "url": "https://prometheus.dev.itlusions.com/", "logo": "/static/img/prometheus_logo.png"},
        ]
        return render_template("index.html", apps=apps)
    
    return app
