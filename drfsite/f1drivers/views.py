from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, \
    IsAuthenticated
from rest_framework.response import Response

from f1drivers.models import Racer, Team
from f1drivers.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from f1drivers.serializers import RacerSerializer

# Create your views here.
# class RacerAPIView(generics.ListAPIView):
#    queryset = Racer.objects.all()
#    serializer_class = RacerSerializer


"""
class RacerViewSet(viewsets.ModelViewSet):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer

    def get_queryset(self):
        return Racer.objects.all()[:3]

    @action(methods=['get'], detail=True)
    def team(self, request, pk=None):
        team = Team.objects.get(pk=pk)
        return Response({'team': team.name})
"""


class RacerAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class RacerAPIList(generics.ListCreateAPIView):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = RacerAPIListPagination


class RacerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class RacerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Racer.objects.all()
    serializer_class = RacerSerializer
    permission_classes = (IsAdminOrReadOnly,)


"""
class RacerAPIView(APIView):
    def get(self, request):
        drivers = Racer.objects.all()
        return Response({"drivers": RacerSerializer(drivers, many=True).data})

    def post(self, request):
        serializer = RacerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"driver": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Racer.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})

        serializer = RacerSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"driver": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            Racer.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Method DELETE not allowed"})

        return Response({"driver": "delete driver " + str(pk)})
"""
