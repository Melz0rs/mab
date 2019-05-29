import redis
import logging
from common.PikaWrapper import PikaWrapper
import common.configurations as configurations

cache = redis.Redis(host='redis', port=6379)
pika_wrapper = PikaWrapper(configurations.rabbit_mq_config['host_name'])


def get_module_logger(mod_name):
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def process_comment(comment):
    logger.info(f"processing comment: {comment}")


def __initialize_queue():
    pika_wrapper.declare_queue(configurations.rabbit_mq_config['comments_queue_name'])


pika_wrapper.start_receiving_messages(queue_name=configurations.rabbit_mq_config['comments_queue_name'],
                                      callback_fn=process_comment)


logger = get_module_logger("__name__")
__initialize_queue()





