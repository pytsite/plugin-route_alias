"""PytSite Route Alias Plugin Events Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router
from . import _api, _error


def router_pre_dispatch():
    """'pytsite.router.pre_dispatch' event handler.
    """
    try:
        p = _api.get_by_alias(_router.request().path)
        _router.add_path_alias(p.alias, p.target)
    except _error.RouteAliasNotFound:
        pass
