from django.contrib.auth.decorators import login_required
from django.urls import  path

from apps.catalogo.view.alga import AlgasListView, AlgasCreateView, AlgasUpdateView
from apps.catalogo.view.especie import EspecieListView, EspecieUpdateView, EspecieCreateView
from apps.catalogo.view.familia import FamiliaListView, FamiliaCreateView, FamiliaUpdateView
from apps.catalogo.view.frutosemilla import FrutoSemillaListView, FrutoSemillaCreateView, FrutoSemillaUpdateView
from apps.catalogo.view.helecho import HelechoListView, HelechoUpdateView, HelechoCreateView
from apps.catalogo.view.hongo import HongoListView, HongoUpdateView, HongoCreateView
from apps.catalogo.view.planta import PlantaListView, PlantaCreateView, PlantaUpdateView
from apps.catalogo.view.polen import PolenListView, PolenCreateView, PolenUpdateView
from apps.catalogo.view.usuario import UsuarioListView, UsuarioCreateView, UsuarioUpdateView
from apps.catalogo.views import HomeViews, PresentacionView, ColeccionView, InvestigacionView, PersonalView

app_name = 'catalogos'



urlpatterns = [
    # URL principal
    path('', HomeViews.as_view(), name="home"),

    # URLs para CRUD usuarios
    path('usuario/', login_required(UsuarioListView.as_view()), name="usuario-list"),
    path('usuario/add/', login_required(UsuarioCreateView.as_view()), name="usuario-add"),
    path('usuario/<int:pk>/edit/', login_required(UsuarioUpdateView.as_view()), name="usuario-edit"),

    # URLs para CRUD Familia
    path('familia/', login_required(FamiliaListView.as_view()), name="familia-list"),
    path('familia/add/', login_required(FamiliaCreateView.as_view()), name="familia-add"),
    path('familia/<int:pk>/edit/', login_required(FamiliaUpdateView.as_view()), name="familia-edit"),

    # URLs para CRUD Especie
    path('especie/', login_required(EspecieListView.as_view()), name="especie-list"),
    path('especie/add/', login_required(EspecieCreateView.as_view()), name="especie-add"),
    path('especie/<int:pk>/edit/', login_required(EspecieUpdateView.as_view()), name="especie-edit"),

    # URLs para CRUD estaticas
    path('presentacion/', login_required(PresentacionView.as_view()), name="presentacion"),
    path('coleccion/', login_required(ColeccionView.as_view()), name="coleccion"),
    path('investigacion/', login_required(InvestigacionView.as_view()), name="investigacion"),
    path('personal/', login_required(PersonalView.as_view()), name="personal"),

    # URLs para CRUD Algas
    path('alga/', login_required(AlgasListView.as_view()), name="alga-list"),
    path('alga/add/', login_required(AlgasCreateView.as_view()), name="alga-add"),
    path('alga/<int:pk>/edit/', login_required(AlgasUpdateView.as_view()), name="alga-edit"),

    # URLs para CRUD Plantas
    path('planta/', login_required(PlantaListView.as_view()), name="planta-list"),
    path('planta/add/', login_required(PlantaCreateView.as_view()), name="planta-add"),
    path('planta/<int:pk>/edit/', login_required(PlantaUpdateView.as_view()), name="planta-edit"),

    # URLs para CRUD Frutos y Semillas
    path('frutosemilla/', login_required(FrutoSemillaListView.as_view()), name="frutosemilla-list"),
    path('frutosemilla/add/', login_required(FrutoSemillaCreateView.as_view()), name="frutosemilla-add"),
    path('frutosemilla/<int:pk>/edit/', login_required(FrutoSemillaUpdateView.as_view()), name="frutosemilla-edit"),

    # URLs para CRUD Polen
    path('polen/', login_required(PolenListView.as_view()), name="polen-list"),
    path('polen/add/', login_required(PolenCreateView.as_view()), name="polen-add"),
    path('polen/<int:pk>/edit/', login_required(PolenUpdateView.as_view()), name="polen-edit"),

    # URLs para CRUD Helecho
    path('helecho/', login_required(HelechoListView.as_view()), name="helecho-list"),
    path('helecho/add/', login_required(HelechoCreateView.as_view()), name="helecho-add"),
    path('helecho/<int:pk>/edit/', login_required(HelechoUpdateView.as_view()), name="helecho-edit"),

    # URLs para CRUD Hongo
    path('hongo/', login_required(HongoListView.as_view()), name="hongo-list"),
    path('hongo/add/', login_required(HongoCreateView.as_view()), name="hongo-add"),
    path('hongo/<int:pk>/edit/', login_required(HongoUpdateView.as_view()), name="hongo-edit"),

]