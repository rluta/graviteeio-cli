import click

@click.command()
@click.argument('api_id', required=True)
@click.pass_obj
def deploy(obj, api_id):
    """deploy api configuration"""
    api_client = obj['api_client']
    resp = api_client.deploy_api(api_id)
    click.echo("API {} is deployed".format(api_id))