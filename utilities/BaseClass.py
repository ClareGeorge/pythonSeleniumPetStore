import inspect
import logging

import pytest



@pytest.mark.usefixtures("initial_setup")
class BaseClass:


    @staticmethod
    def getLogger(filehandler):
        log = logging.getLogger("TestCase: " + inspect.stack()[1][3])
        log.addHandler(filehandler)
        log.setLevel(logging.DEBUG)
        return log