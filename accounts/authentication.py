from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

class EmailOTPBackend(ModelBackend):
    def authenticate(self, request, email=None, otp=None, **kwargs):
        User = get_user_model()
        try:
            # Retrieve the user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        # Verify the OTP code
        user_profile = user.user_profile
        if user_profile.otp_code == otp:
            return user

        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
