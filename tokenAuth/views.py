from datetime import timedelta
import secrets
from .models import tokenAuth
from users.models import Student
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone  # Import timezone from Django utils
import jwt

# generate token (login)
def create_token(user, type):
    # Refresh every 2 hours, return same token if still in same 2 hours
    try:
        existent_token = tokenAuth.objects.get(user=user)
    except ObjectDoesNotExist:
        existent_token = None
    
    if existent_token:
        if existent_token.expiration_time > timezone.now():  # Retrieve same token
            existent_token.active = True
            existent_token.save()
            return existent_token.token
        else:
            existent_token.delete()
    # Generate a random secret key
    secret_key = secrets.token_urlsafe(32)

    # Set the expiration time for the token (e.g., 2 hours from now)
    expiration_time = timezone.now() + timedelta(hours=2) 

    # Create the payload
    payload = {
        "email": user.email,
        "exp": expiration_time.timestamp(),  # Convert expiration_time to a timestamp
    }

    # Generate the JWT
    secret_token = jwt.encode(payload, secret_key, algorithm="HS256")
    
    if type == "student":
        secret_token = "s"+secret_token
    elif type == "professor":
        secret_token = "p" + secret_token

    # Store the JWT in the database along with its expiration time
    tokenAuth.objects.create(
        user=user, token=secret_token, expiration_time=expiration_time, active=True
    )

    return secret_token


# delete token (logout)
def delete_token(token):
    if not token:
        return False
    try:
        previous_jwt = tokenAuth.objects.get(token=token)
        previous_jwt.delete()
        return True

    except tokenAuth.DoesNotExist:
        return False


# check connectivity (every request)
def check_token(got_token):
    if not got_token:
        print("no token")
        return False
    try:
        user_jwt = tokenAuth.objects.get(token=got_token)
        user = Student.objects.get(id=user_jwt.user.id)  # Access user_id directly
        if timezone.now() > user_jwt.expiration_time:  #token expired
            user_jwt.delete()
            return False
        elif not user_jwt.active:
            return False
        return user
    except ObjectDoesNotExist:
        return False
    except Exception as e:
        print(e)
        return False
    
