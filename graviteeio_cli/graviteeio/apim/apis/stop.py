import click

@click.command()
@click.argument('api_id', required=True)
@click.pass_obj
def stop(obj, api_id):
    """stop api"""
    api_client = obj['api_client']
    resp = api_client.stop_api(api_id)
    click.echo("API {} is stopped".format(api_id))