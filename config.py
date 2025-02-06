import logging


def log_config(level):
    logging.basicConfig(
        level=level,
        format="%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s",
    )
