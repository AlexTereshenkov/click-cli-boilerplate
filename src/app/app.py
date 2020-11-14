import click
from src.app.worker import _add, _help
from src import __cliversion__

# this is used to allow "sample-cli add -h" and "sample-cli add --help"
HELP_OPTS = dict(help_option_names=["-h", "--help"])


@click.group()  # add epilog="" if required
@click.version_option(__cliversion__)
@click.pass_context
def cli(ctx: click.Context):
    """Main entrance point."""
    # https://stackoverflow.com/a/44079245/3346915
    # if want to make command arguments available in the cli group
    # to be able to inspect the context:
    # if "add" in ctx.obj:
    #     click.echo("Calling add command...")
    return


@cli.command()
def man():
    """Man page for all commands of the cli."""
    _help(cli)


@cli.command(context_settings=HELP_OPTS)
@click.option("--numbers",
              "numbers",
              help="Two numbers to add together",
              nargs=2,
              required=True)
def add(numbers):
    """Add two numbers together."""
    result = _add(int(numbers[0]), int(numbers[1]))
    click.secho(str(result), fg="green")
