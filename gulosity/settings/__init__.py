from common import *

try:
    from dev import *
    from test import *
except:
    pass

if not DEBUG:
    try:
        from prod import *
    except:
        pass
