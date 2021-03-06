from pprint import pprint

from huaweisms.api import monitoring, user, device
from huaweisms.api.common import ApiCtx


USER = "admin"
PASSWORD = "admin123"

# BEFORE running, do MAKE SURE heaweisms.api.config has the CORRECT VALUES for your MODEM


def get_session():
    return user.quick_login(USER, PASSWORD)


def valid_context(ctx):
    # type: (ApiCtx) -> bool
    sl = user.state_login(ctx)
    if sl['type'] == 'response' and sl['response']['State'] != -1:
        return True
    return False


ctx = get_session()

sent = device.reboot(ctx)
print(sent)
