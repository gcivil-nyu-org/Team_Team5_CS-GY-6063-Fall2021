# from django.test import TestCase
# from cal.tests.test_forms import *
# from cal.tests.test_models import *
# from cal.tests.test_utils import *
# from cal.tests.test_views import *
# from yelp_search.tests.test_views import *
# from accounts.tests.test_models import *
# from accounts.tests.test_views import *
# from accounts.tests.test_tokens import *
# from accounts.tests.test_forms import *

import pkgutil
import unittest

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(module_name).load_module(module_name)
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, unittest.case.TestCase):
            exec("%s = obj" % obj.__name__)


def suite():
    return unittest.TestLoader().discover("accounts.tests", pattern="*.py")
