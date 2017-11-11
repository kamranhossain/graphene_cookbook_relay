from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&a=b0f7$-n^$r2szk$-%jtyalc+fy%-j5h2j^0$*9xkktv4ic('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)
