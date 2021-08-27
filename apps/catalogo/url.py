from django.contrib.auth.decorators import login_required
from django.urls import  path

from apps.catalogo.view.alga import AlgasListView, AlgasCreateView, AlgasUpdateView
from apps.catalogo.view.familia import FamiliaListView, FamiliaCreateView, FamiliaUpdateView
from apps.catalogo.view.usuario import UsuarioListView, UsuarioCreateView, UsuarioUpdateView
from apps.catalogo.views import HomeViews, PresentacionView

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

    # URLs para CRUD estaticas
    path('presentacion/', login_required(PresentacionView.as_view()), name="presentacion"),

    # URLs para CRUD Algas
    path('alga/', login_required(AlgasListView.as_view()), name="alga-list"),
    path('alga/add/', login_required(AlgasCreateView.as_view()), name="alga-add"),
    path('alga/<int:pk>/edit/', login_required(AlgasUpdateView.as_view()), name="alga-edit"),

]