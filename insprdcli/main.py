import os

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal

from .controllers.base import Base
from .controllers.publisher import Publisher
from .core.exc import InsprdCLIError
from .utils import get_config_dir


# configuration defaults
CONFIG = init_defaults('insprd')


class InsprdCLI(App):
    """Inspired CLI primary application."""

    class Meta:
        label = 'insprdcli'

        # configuration defaults
        config_defaults = CONFIG
        config_section = 'insprd'

        config_files = [
            os.path.join(get_config_dir(), 'publishers'),
        ]

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'colorlog',
            'jinja2',
            'yaml',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        #config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Publisher,
        ]


class InsprdCLITest(TestApp,InsprdCLI):
    """A sub-class of InsprdCLI that is better suited for testing."""

    class Meta:
        label = 'insprdcli'


def main():
    with InsprdCLI() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except InsprdCLIError as e:
            print('InsprdCLIError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
