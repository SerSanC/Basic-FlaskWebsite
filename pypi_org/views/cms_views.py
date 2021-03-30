import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service

blueprint = flask.Blueprint('cs', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    print("getting CMS page for {}".format(full_url))
    page = cms_service.get_page(full_url)
    if not page:
        flask.abort(404)
    return page
