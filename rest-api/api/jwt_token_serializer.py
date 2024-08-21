from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JwtTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id
        token['email'] = user.email

        return token
