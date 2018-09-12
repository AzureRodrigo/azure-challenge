from django.contrib.auth.models import User


# Classe chamada ao tentar efetuar login
class EmailLoginBackend(object):
    # método de override da autenticação, para tornar possivel logar por email e não nome
    @staticmethod
    def authenticate(self, email=None, password=None):
        try:
            # busca o usuário no db pelo email
            user = User.objects.get(email=email)
            # verifica se a senha esta correta para esse usuário
            success = user.check_password(password)

            if success:
                return user
        except User.DoesNotExist:
            return None
        return None

    # método de override da autenticação, chamado para pegar o usuário pelo "id"
    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except():
            return None
