import subprocess

GLOBAL_PREFIX: [str] = ['ssh', 'root@localhost', 'lxc', 'exec', 'switch1', '--']


def run_command(cmd: [str]) -> (int, str):
    result = subprocess.run(GLOBAL_PREFIX + cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    code = result.returncode
    return code, output
