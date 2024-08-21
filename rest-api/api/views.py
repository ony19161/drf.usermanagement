from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view


from .jwt_token_serializer import JwtTokenSerializer


def authenticate(username=None, password=None):
    try:
        user = User.objects.get(username=username)
        if user.password == password:
            return user
        else:
            return None
    except User.DoesNotExist:
        return None


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
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        tokens = get_tokens_for_user(user)
        response_data = {
            'tokens': tokens
        }
        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=401)


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
