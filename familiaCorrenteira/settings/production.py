from .settings import *
import random, string


def generate():
    uni = string.ascii_letters + string.digits + string.punctuation
    key = ''.join([random.SystemRandom().choice(uni) for _ in range(random.randint(45, 50))])
    return key

DEBUG = False
SECRET_KEY = generate()