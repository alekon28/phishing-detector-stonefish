""" Module contain a redis client """

import os

from redis import Redis


class RedisClient:
    """ Redis client """
    def __init__(self):
        self.client = Redis(
            db=0,
            host=os.environ.get('REDIS_HOST') or 'localhost',
            port=int(os.environ.get('REDIS_PORT') or 6379)
        )
