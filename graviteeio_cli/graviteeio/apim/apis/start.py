import click

@click.command()
@click.argument('api_id', required=True)
@click.pass_obj
def start(obj, api_id):
    """start api"""
    api_client = obj['api_client']
    resp = api_client.start_api(api_id)
    click.echo("API {} is started".format(api_id))