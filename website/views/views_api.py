from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from website.models import Register
from website.api.serializers import RegisterSerializer


class GetRegisterView(viewsets.ModelViewSet):
    # só exibe os dados caso usuário esteja autenticado e autorizado
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    # serializa os dados
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['get']

    # função responsavel por buscar os registros e serializar
    def get(self, request, format=None):

        queryset = Register.objects.all()

        serializer = self.serializer_class(request, queryset, self, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostRegisterView(viewsets.ModelViewSet):
    # só exibe os dados caso usuário esteja autenticado e autorizado
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    # serializa os dados
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    # função responsavel por serializar e enviar os dados ao servidor
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
