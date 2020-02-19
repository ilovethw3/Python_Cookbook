import logging
logging.disable(10)
logger=logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
handler=logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.disable(50)

if __name__=="__main__":
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail")
    logger.error("Something is error")
    logger.critical("Something is very very critical")
    logger.info("Finish")