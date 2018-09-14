from os import path

from restfulpy.testing import ApplicableTestCase

from odin import Odin


class LocalApplicationTestCase(ApplicableTestCase):
    __application_factory__ = Odin

