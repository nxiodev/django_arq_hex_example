from rest_framework.exceptions import ValidationError

from apps.backoffice.models import Administrator


def change_password_user(user, old_password, new_password):
    if not user.check_password(old_password):
        raise ValidationError({'old_password': 'La contraseña actual no es correcta'})

    user.set_password(new_password)
    user.save()

def recovery_password_user(username: str, email: str, new_password: str):
    try:
        user = Administrator.objects.get(username=username, email=email)
    except Administrator.DoesNotExist:
        raise ValidationError({'username': 'Usuario o correo incorrecto'})

    user.set_password(new_password)
    user.save()
    return True
