import os
from init_app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host=os.environ.get("IP_OR_DOMAIN"), port=int(os.environ.get("PORT")))
