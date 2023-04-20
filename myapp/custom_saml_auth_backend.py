from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomSAMLAuthBackend(ModelBackend):
    def find_user(self, user_data):
        """Encuentra un usuario en función del nombre y correo electrónico."""

        UserModel = get_user_model()

        username = user_data.get('username')
        email = user_data.get('email')

        if not username and not email:
            return None

        try:
            user = UserModel.objects.get(username=username, email=email)
        except UserModel.DoesNotExist:
            # Si no se encuentra un usuario, se crea uno nuevo
            user = UserModel.objects.create_user(username=username, email=email)

        return user

