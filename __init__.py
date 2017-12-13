"""PytSite Route Alias Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import create, find, get_by_target, get_by_alias
    from . import _model as model, _error as error


def plugin_load():
    from pytsite import router
    from plugins import odm
    from . import _eh

    odm.register_model('route_alias', model.RouteAlias)
    router.on_pre_dispatch(_eh.router_pre_dispatch)
