"""PytSite Route Alias Plugins Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router, lang as _lang
from plugins import odm as _odm


class RouteAlias(_odm.model.Entity):
    """Route Alias Model.
    """

    def _setup_fields(self):
        """Hook.
        """
        self.define_field(_odm.field.String('alias', is_required=True))
        self.define_field(_odm.field.String('target', is_required=True))
        self.define_field(_odm.field.String('language', is_required=True, default=_lang.get_current()))

    def _setup_indexes(self):
        """Hook.
        """
        self.define_index([('alias', _odm.I_ASC), ('language', _odm.I_ASC)], unique=True)

    @property
    def alias(self) -> str:
        return self.f_get('alias')

    @property
    def target(self) -> str:
        return self.f_get('target')

    @property
    def language(self) -> str:
        return self.f_get('language')

    def _on_f_set(self, field_name: str, value, **kwargs):
        """Hook.
        """
        if field_name == 'alias':
            from . import _api
            value = _api.sanitize_alias_string(value, self.language, None if self.is_new else self)

        return super()._on_f_set(field_name, value, **kwargs)

    def _on_after_delete(self, **kwargs):
        """Hook.
        """
        _router.remove_path_alias(self.alias)

    def as_jsonable(self, **kwargs) -> dict:
        r = super().as_jsonable(**kwargs)

        r.update({
            'language': self.language,
            'alias': self.alias,
            'target': self.target,
        })

        return r
