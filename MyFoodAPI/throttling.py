from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class DKThrottle(UserRateThrottle):
    scope = 'DK'
