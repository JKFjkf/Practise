# -*- coding: utf-8 -*-
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("logs/log_%s.txt" % (time.strftime("%Y-%m-%d", time.localtime())))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
# -*- coding: utf-8 -*-
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("logs/log_%s.txt" % (time.strftime("%Y-%m-%d", time.localtime())))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")