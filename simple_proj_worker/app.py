import redis
import logging

cache = redis.Redis(host='redis', port=6379)


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    prev_count = 0
    logger = get_module_logger("__name__")

    while True:
        new_count = cache.get("notifications_count")

        if prev_count != new_count:
            prev_count = new_count

            logger.info(f"new count: {new_count}")
