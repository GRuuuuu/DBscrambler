import click


class Ddd:
    def __init__(self, ddd):
         self.state=ddd

    def print(self):
         print(self.state)


@click.command(help="fffffff")
@click.option('--p',default=1, help='ppppppp')
def fff(p):
    print(p)


@click.group()
def cli():
    pass

@click.command(help="statedd")
@click.option('--state',default=1, help='state')
def dbscram(state):
    res=Ddd(state)
    res.print()

cli.add_command(fff)
cli.add_command(dbscram)
cli()
