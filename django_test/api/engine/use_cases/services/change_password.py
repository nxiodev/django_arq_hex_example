from rest_framework.exceptions import ValidationError


def change_password_user(user, old_password, new_password):
    if not user.check_password(old_password):
        raise ValidationError({'old_password': 'La contraseña actual no es correcta'})

    user.set_password(new_password)
    user.save()