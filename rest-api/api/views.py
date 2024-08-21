from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view


from .jwt_token_serializer import JwtTokenSerializer


def get_tokens_for_user(user):
    refresh = JwtTokenSerializer.get_token(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there, this is Django API response!!"
    })


@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Generate JWT Token
        tokens = get_tokens_for_user(user)
        return JsonResponse({
            'tokens': tokens
        })
    else:
        return JsonResponse({
            "message": "Sign up failed"
        })


@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse({
        'users': serializer.data
    })
