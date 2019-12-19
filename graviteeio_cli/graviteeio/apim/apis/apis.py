import click
import os
import sys

from ..client.api import api_client

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'plugins'))
add_command = ["ps", "init", "start", "stop", "deploy", "update", "create"]

class PluginCommand(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.extend(add_command)
        rv.sort()
        
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            if name in add_command:
                mod = __import__('graviteeio_cli.graviteeio.apim.apis.' + name, None, None, [name])
            else:
                mod = __import__('graviteeio_cli.graviteeio.apim.apis.plugins.cmd_' + name, None, None, [name])
        except ImportError:
            return
        return getattr(mod,name)


@click.command(cls=PluginCommand)
@click.pass_context
def apis(ctx):
    ctx.obj['api_client'] = api_client(config=ctx.obj['config'])

