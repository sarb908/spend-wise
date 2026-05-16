# verify_password(plain_password: str, hashed_password: str) -> bool

# get_password_hash(password: str) -> str


from passlib.context import CryptContext


pwd_cxt = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


def get_password_hash(password: str) -> str:
    return pwd_cxt.hash(password)




def verify_password(plain_password: str, hashed_password: str) -> bool:


    return pwd_cxt.verify(plain_password, hashed_password)