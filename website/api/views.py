from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from website.models import Register
from website.api.serializers import RegisterSerializer
from website.api.filters import RegisterFilter


# View responsável por exibir e inserir novos registros
class RegisterView(APIView):
    # só exibe os dados caso usuário esteja autenticado e autorizado
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    # serializa os dados
    serializer_class = RegisterSerializer

    # campos que podem ser informados no filtro
    filter_fields = ('name', 'cost')

    # função responsavel por buscar os registros e serializar
    def get(self, request, format=None):

        queryset = Register.objects.all()
        filter = RegisterFilter()

        serializer = self.serializer_class(filter.filter_queryset(request, queryset, self), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # função responsavel por serializar e enviar os dados ao servidor
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
