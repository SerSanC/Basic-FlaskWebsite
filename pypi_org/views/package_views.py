import flask

from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/projects/<package_name>')
@response(template_file='packages/details.html')
def index():
    return "Package details for {}".format()
