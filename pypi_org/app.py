import flask
from flask import Flask

app = Flask(__name__)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)

"""
El motivo de utilizar el if - else para la ejecución de inicio, es que por defecto en la configuración del PyCharm levanta un servidor, entonces si no usamos PyCharm entrará por el if
"""
if __name__ == '__main__':
    register_blueprints()
    app.run(debug=True)
else:
    register_blueprints()
