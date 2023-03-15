""" Module contain a redis client """

from redis import Redis


class RedisClient:
    """ Redis client """
    def __init__(self):
        self.client = Redis(db=0, host='localhost', port=6379)
