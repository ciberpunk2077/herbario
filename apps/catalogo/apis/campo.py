from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalogo.models import Planta

class PlantaDeleteApiView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('pk') and self.kwargs.get('pk') != '':
                Planta.objects.get(pk=self.request.POST.get('pk')).delete()
                return Response(data={'error': 0, 'message': 'El registro ha sido removido de la lista con éxito.'}, status=200)
            else:
                return Response(data={'error': 1, 'message': 'El objeto es requerido, inténtelo nuevamentes'}, status=200)
        except Exception as E:
            return Response(data={'error': 3, 'message': 'Ha ocurrido un error interno, inténtelo nuevamente.'}, status=500)
        return Response(data={'error': 2, 'message': 'La opereación no fué procesada, inténtelo nuevamente.'}, status=200)




