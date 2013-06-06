from django.contrib.auth.backends import ModelBackend

from lazysignup.models import LazyUser


class LazySignupBackend(ModelBackend):

    def authenticate(self, username=None):
        """This method will always authenticate the given user."""

        UserModel = LazyUser.get_user_class()
        #if username is None:
        #    username_field = getattr(UserModel, 'USERNAME_FIELD', 'username')
        #    username = kwargs.get(username_field)
        try:
            return UserModel.objects.get(username=username)
            #if callable(UserModel._default_manager.get_by_natural_key):
            #    return UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Annotate the user with our backend.

        This way the backend is always available, not just when authenticate()
        has been called. This will be used by the is_lazy_user filter.

        """
        UserModel = LazyUser.get_user_class()
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            user = None
        else:
            user.backend = 'lazysignup.backends.LazySignupBackend'
        return user
