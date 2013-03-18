from django.conf import settings

ACCESS_CONTROL_ALLOW_ORIGIN = getattr(settings, "ACCESS_CONTROL_ALLOW_ORIGIN", [])
access_control_allow_origin = ", ".join(ACCESS_CONTROL_ALLOW_ORIGIN)