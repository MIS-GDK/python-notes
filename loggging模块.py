import logging


logging.basicConfig(
    filename=r"E:\log.txt",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y/%m/%d %X",
)
logging.debug("this is debug")
logging.info("this is info")
logging.error("this is error")
