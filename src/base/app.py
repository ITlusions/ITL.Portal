import os
from flask import Flask, render_template

def create_app():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    
    robots_txt_path = os.path.join(parent_dir, 'robots.txt')
    # Create the Flask app instance
    app = Flask(__name__, static_folder=os.path.join(parent_dir, 'static'), template_folder=os.path.join(parent_dir, 'templates'))

    # Application configurations can be added here
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Set up static and template directories (Flask automatically uses 'static' and 'templates')
    # If needed, customize the paths here, but this is the default behavior

    @app.route("/")
    def dashboard():
        # Sample app data
        apps = [
            {"name": "ArgoCD", "url": "https://argocd.dev.itlusions.nl/", "logo": "https://argocd.dev.itlusions.nl/assets/images/argo_o.svg"},
            {"name": "GIT", "url": "https://git.dev.itlusions.nl/", "logo": "https://git.dev.itlusions.nl/assets/img/logo.svg"},
            {"name": "Longhorn", "url": "https://longhorn.dev.itlusions.nl/", "logo": "https://ranchergovernment.com/hs-fs/hubfs/Longhorn%201.png?width=389&height=319&name=Longhorn%201.png", "logo_black": "/static/img/longhorn-dark.png"},
            {"name": "Grafana", "url": "https://Grafana.dev.itlusions.nl/", "logo": "/static/img/grafana-icon.svg"},
        ]
        return render_template("index.html", apps=apps)
    
    return app
