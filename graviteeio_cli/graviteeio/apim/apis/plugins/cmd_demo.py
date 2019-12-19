import click


@click.command('demo', short_help='Shows how to create a plugin')
def demo():
    """Shows file changes in the current working directory."""
    click.echo("Demoooooo")