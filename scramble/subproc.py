import subprocess

def preproc(orig, parsed):
    with open(parsed, 'wb') as f:
        out = subprocess.run(['./scramble/preproc',orig], capture_output=True)
        f.write(out.stdout)

def valid(sql,result):
    with open(result, 'wb') as f:
        out = subprocess.run(['sh','-x','./scramble/valid.sh',sql], capture_output=True)
        f.write(out.stdout)