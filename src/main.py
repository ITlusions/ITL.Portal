import os, sys
from base.app import create_app

app = create_app()

if __name__ == '__main__':
    
    # If the script is run directly, start the Gunicorn server
    if 'gunicorn' in sys.modules:
        port = int(os.getenv('FLASK_RUN_PORT', 80))
        debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
        
        # Set the environment variable for Gunicorn to run the app
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    else:
        # You can optionally run with the Flask development server if needed
        port = int(os.getenv('FLASK_RUN_PORT', 81))
        debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
        app.run(host='0.0.0.0', port=port, debug=debug_mode)