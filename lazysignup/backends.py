from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class LazySignupBackend(ModelBackend):

    def authenticate(self, username=None):
        """This method will always authenticate the given user."""

        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            return UserModel._default_manager.get_by_natural_key(username)
        except user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Annotate the user with our backend.

        This way the backend is always available, not just when authenticate()
        has been called. This will be used by the is_lazy_user filter.

        """
        user = super(LazySignupBackend, self).get_user(user_id)
        if user is not None:
            user.backend = 'lazysignup.backends.LazySignupBackend'
        return user
