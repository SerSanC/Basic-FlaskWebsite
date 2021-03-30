import os

from flask import Flask

import pypi_org.data.db_session as db_session

app = Flask(__name__)


def setup_db():
    print("Llegamos a  db")
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite'
    )
    db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


"""
El motivo de utilizar el if - else para la ejecución de inicio, es que por defecto en la configuración del PyCharm levanta un servidor, entonces si no usamos PyCharm entrará por el if
"""
if __name__ == '__main__':
    register_blueprints()
    setup_db()
    app.run(debug=True)
else:
    register_blueprints()
    setup_db()
