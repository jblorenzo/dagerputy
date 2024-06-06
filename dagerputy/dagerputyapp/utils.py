from django.contrib.auth import get_user_model


def dagerputy_needs_setup():
    return not get_user_model().objects.all().exists()
