from rest_framework.throttling import UserRateThrottle

class MinuteRateThrottle(UserRateThrottle):
    scope = 'user_minute'