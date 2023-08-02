import subprocess

GLOBAL_PREFIX: [str] = []  # ['ssh', 'root@localhost', 'lxc', 'exec', 'vpn1', '--']


def run_command(cmd: [str]) -> (int, str):
    print(" ".join(cmd))
    result = subprocess.run(GLOBAL_PREFIX + cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    code = result.returncode
    print(str(code)+": "+output)
    return code, output
