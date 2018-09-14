from nanohttp import Controller, json
from restfulpy.controllers import RootController

import odin

class Apiv1(Controller):

    @json
    def version(self):
        return dict(version=odin.__version__)


class Root(RootController):
    apiv1 = Apiv1()
