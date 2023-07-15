from esmf_server.impl.command_util import run_command


class WireguardKeygen(object):
    @classmethod
    def gen_keys(cls):
        ec, private_key = run_command(["wg", "genkey"])
        if ec != 0:
            raise Exception(f"Error while generating key: {ec} - {private_key}")
        ec, public_key = run_command(["sh", "-c", f"\"echo \\\"{private_key}\\\" | wg pubkey\""])
        if ec != 0:
            raise Exception(f"Error while exporting public key from private key: {ec} - {public_key}")
        return private_key, public_key
