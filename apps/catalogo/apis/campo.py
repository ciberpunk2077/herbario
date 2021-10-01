from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalogo.models import Planta, Algas, FrutoSemilla, Polen, Helecho, Hongo, Familia, Especie,User


class PlantaDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                planta = Planta.objects.get(pk=self.request.POST.get('pk'))
                planta.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'}, status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'}, status=200)


class AlgasDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                alga = Algas.objects.get(pk=self.request.POST.get('pk'))
                alga.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'}, status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'}, status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'}, status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'}, status=200)

class FrutoSemillaDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                frutosemilla = FrutoSemilla.objects.get(pk=self.request.POST.get('pk'))
                frutosemilla.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)


class PolenDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                polen = Polen.objects.get(pk=self.request.POST.get('pk'))
                polen.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)
class HelechoDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                helecho = Helecho.objects.get(pk=self.request.POST.get('pk'))
                helecho.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)

class HongoDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                hongo = Hongo.objects.get(pk=self.request.POST.get('pk'))
                hongo.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)

class FamiliaDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                familia = Familia.objects.get(pk=self.request.POST.get('pk'))
                familia.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)

class EspecieDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                especie = Especie.objects.get(pk=self.request.POST.get('pk'))
                especie.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)

class UsuarioDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('pk') and self.request.POST.get('pk') != '':
                usuario = User.objects.get(pk=self.request.POST.get('pk'))
                usuario.delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'},
                                status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'},
                                status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'},
                            status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'},
                        status=200)