import subprocess

from esmf_server.impl.command_util import run_command


class WireguardKeygen(object):
    @classmethod
    def gen_keys(cls):
        ec, private_key = run_command(["wg", "genkey"])
        if ec != 0:
            raise Exception(f"Error while generating key: {ec} - {private_key}")
        private_key = private_key.replace("\n", "")
        public_key = subprocess.getoutput(f'echo "{private_key}" | wg pubkey').replace("\n", "")
        return private_key, public_key
