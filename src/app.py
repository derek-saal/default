import logging
import sys
from pathlib import Path

import connexion
from flask import Flask
from flask_cors import CORS

this_file = Path(__file__)
proj_dir = Path(__file__).parents[1]
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')
module_logger = logging.getLogger(proj_dir.stem + '.' + str(this_file.stem))
fh = logging.FileHandler(this_file.with_suffix('log'), mode='w')
module_logger.addHandler(fh)


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
