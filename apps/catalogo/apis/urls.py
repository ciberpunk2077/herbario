from django.urls import path

from .campo import *

app_name = 'catalogo-api'

urlpatterns = [
    path('api/campos_planta/remove/', PlantaDeleteApiView.as_view(), name="api-planta-remove"),
    path('api/campos_algas/remove', AlgasDeleteApiView.as_view(), name="api-alga-remove"),
    path('api/campos_frutos/remove', FrutoSemillaDeleteApiView.as_view(), name="api-frutosemilla-remove"),
    path('api/campos_polen/remove/', PolenDeleteApiView.as_view(), name="api-polen-remove"),
    path('api/campos_helecho/remove/', HelechoDeleteApiView.as_view(), name="api-helecho-remove"),
    path('api/campos_hongo/remove/', HongoDeleteApiView.as_view(), name="api-hongo-remove"),
    path('api/campos_familia/remove/', FamiliaDeleteApiView.as_view(), name="api-familia-remove"),
    path('api/campos_especie/remove/', EspecieDeleteApiView.as_view(), name="api-especie-remove"),
    path('api/campos_usuario/remove/', UsuarioDeleteApiView.as_view(), name="api-usuarios-remove"),

]
