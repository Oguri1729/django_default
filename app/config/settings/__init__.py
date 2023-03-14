
from .allauth import *
from .user import *
from .path import *
from .secret import *
from .settings import *
from .url import *


DEBUG = True


if DEBUG:
    from .debug import *
else:
    from .production import *
