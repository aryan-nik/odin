from os.path import join, dirname

from restfulpy import Application

from .controllers import Root


__version__ = '0.1.0-dev1'


class Odin(Application):
    __configuration__ = '''
    db:
        url: postgres://postgres:postgres@localhost/dolphin_dev
        test_url: postgres://postgres:postgres@localhost/dolphin_test
        administrative_url: postgres://postgres:postgres@localhost/postgres
    '''

    def __init__(self, application_name='dolphin', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=join(dirname(__file__), '..'),
            version=__version__
        )


odin = Odin()

