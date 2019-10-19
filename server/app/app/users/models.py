from django.contrib.auth.models import AbstractUser
from django.db.models import (
    ImageField,
    DateTimeField
)


class User(AbstractUser):
    """
    # https://docs.djangoproject.com/ja/2.1/ref/contrib/auth/#django.contrib.auth.models.User

    Note:
    If you add another field in User model, you should edit CustomSignupForm class in app/account/forms.py
    """

    image = ImageField(blank=True, null=True, upload_to="images/users/")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
