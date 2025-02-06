import logging

import redis

from config import log_config

log = logging.getLogger(__name__)
log_config(logging.DEBUG)


def main():
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Проверка подключения
    try:
        r.ping()
        log.info('Подключение к Redis успешно!')
    except redis.ConnectionError as e:
        log.error('Ошибка подключения к Redis. %s', e, exc_info=True)
        return

    r.set('user1', 'user1')
    user1 = r.get('user1')

    log.info(user1)
    log.info(user1.decode('utf-8'))

    # ------------------------

    r.incr('counter')
    log.info('Счетчик: %s', r.get('counter'))

    # ------------------------

    r.lpush('list1', 'item1')
    r.lpush('list1', 'item2')

    log.info(type(r.lrange('list1', 0, -1)))
    log.info('Список list1: %s', r.lrange('list1', 0, -1))

    # ------------------------

    r.hset('user:1', 'name', 'Anton')
    r.hset('user:1', 'gender', 'male')

    log.info(type(r.hgetall('user:1')))
    log.info(r.hgetall('user:1'))


if __name__ == '__main__':
    main()
    # while True:
    #     pass
