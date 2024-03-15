from passlib.context import CryptContext
from bcrypt import __version__ as bcrypt_version

def _load_backend_mixin():
    version = bcrypt_version
    # Rest of your code

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)