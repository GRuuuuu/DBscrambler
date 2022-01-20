import click
from scramble import scramb
from scramble import primary_check
from scramble import subproc

@click.group()
def cli():
    pass

@click.command(help="parse each SELECT line into multi line")
@click.option('--orig',default=None, type=click.Path(exists=True), help='add file path to the commands to store original sql dump file')
@click.option('--parsed',default=None, help='add file path to the commands to store parsed sql dump file')
def parse(orig, parsed):
    subproc.preproc(orig, parsed)


@click.command(help="scramble the data from parsed sql dump")
@click.option('--file',default=None, type=click.Path(exists=True), help='add \"PARSED\" sql dump file to the commands to be scrambled')
@click.option('--yaml',default=None, type=click.Path(exists=True), help='add metadata-yaml file to the commands to provide information on how to scramble')
@click.option('--output_scrambled',default=None,help='filepath where scrambled sql dump file is stored')
@click.option('--output_blank',default=None,help='filepath where scrambled data erased sql dump file is stored')
def dbscramb(file,yaml,output_scrambled,output_blank):
    masker = scramb.DBScramble(dumpfile=file,
                                infofile=yaml,
                                outfile_scrambled=output_scrambled,
                                outfile_blank=output_blank)
    masker.parse()


@click.command(help="validate each column in metadata-yaml whether It is correct or primary key or unique key")
@click.option('--file',default=None, type=click.Path(exists=True), help='add sql dump file to the commands to provide column information')
@click.option('--yaml',default=None, type=click.Path(exists=True), help='add metadata-yaml file to the commands to validate')
def prechk(file,yaml):
    pc = primary_check.DBPrimaryCheck(dumpfile=file,
                                    ymlfile=yaml)
    yml_info = pc.primary_check()
    print(yml_info)


@click.command(help="validate any exist PI in scrambled sql dump file")
@click.option('--sql',default=None, type=click.Path(exists=True), help='add scrambled dump file path to commands to detect PI')
@click.option('--result',default=None, help='add file path to commands to store result')
def valid(sql,result):
    subproc.valid(sql,result)


cli.add_command(parse)
cli.add_command(prechk)
cli.add_command(dbscramb)
cli.add_command(valid)
cli()