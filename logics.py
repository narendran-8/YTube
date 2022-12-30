from passlib.context import CryptContext

# to check password and conform password
def password_check(password, c_password):
    if password == c_password:
        return True
    else:
        return False

#------------------------------------------------
# Hash the password
def hash_password(password):
    pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pass_context.hash(password)