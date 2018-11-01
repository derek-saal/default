import logging
import sys
from pathlib import Path

import connexion
from flask import Flask
from flask_cors import CORS

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
# ToDo Fill in project name
module_logger = logging.getLogger('project.app')
proj_dir = Path(__file__).parents[1]


def get_health_check():
    module_logger.info(f"Got Heath Check request")
    return True, 200


app = connexion.App(__name__)
app.add_api('swagger.yaml')
if __name__ == '__main__':
    port = 8080

    print(f"Please go to: http://localhost:{str(port)}/ui/")
    # add CORS support
    CORS(app.app)
    app.run(port=port)
