from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalogo.models import Familia


class FamiliaStatusApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('pk') and self.kwargs.get('pk') != '':
                familia = Familia.objects.get(pk=self.request.POST.get('pk'))
                familia.activo = True if self.request.POST.get('status') == 'true' else False
                familia.save()
                return Response(data={'error': 0, 'message': 'El registro ha sido actualizado con éxito.'}, status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'}, status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'}, status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'}, status=200)
