import click


def _add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: A sum of two numbers.
    """
    return a + b


def _help(cmd, parent=None) -> None:
    """Generate a help page for all cli commands."""
    # https://stackoverflow.com/a/58018765/3346915
    # to generate a help page for all cli commands
    ctx = click.core.Context(cmd, info_name=cmd.name, parent=parent)
    print(cmd.get_help(ctx))
    print('-' * 60)
    commands = getattr(cmd, 'commands', {})
    for sub in commands.values():
        _help(sub, ctx)
