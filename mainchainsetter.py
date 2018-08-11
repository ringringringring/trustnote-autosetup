import json

from tools import Tools

#home_path = "/home/houfa"
home_path = "D:\\Code\\ThingTrust"
source_path = "{0}/mainchain".format(home_path)
testnet_builder_path = "{0}/testnet-builder".format(source_path)
testnet_builder_data_path = "{0}/data".format(testnet_builder_path)
trustnote_headless_path = "{0}/trustnote-headless".format(testnet_builder_path)
trustnote_headless_play_path = "{0}/play".format(trustnote_headless_path)
trustnote_hub_path = "{0}/trustnote-hub".format(testnet_builder_path)
trustnote_witness_path = "{0}/trustnote-witness".format(testnet_builder_path)
trustnote_explorer_path = "{0}/trustnote-explorer".format(testnet_builder_path)
config_path = "{0}/.config".format(home_path)
shell_path = "{0}/shell".format(source_path)

old_first_utxo = "IO3JFSLJQVS4GNWR6I4QYIPBYGIUF3ZF"
old_from_address = "IO3JFSLJQVS4GNWR6I4QYIPBYGIUF3ZF"
old_payee_address= "XIM76DRNUNFWPXPI5AGOCYNMA3IOXL7V"

class MainChainSetter:
    """Setup main chain run environment."""
    first_utxo = ""
    from_address = ""
    payee_address = ""
    all_addresses = []
    headless_addresses = []
    witness_addresses = []

    def __init__(self):
        return

    def setup_os_env(self):
        Tools.run_shell_command("sudo {0}/setup_os_env.sh".format(shell_path))
        return

    def load_code(self):
        Tools.run_shell_command("sudo {0}/loadcode.sh".format(shell_path))
        return
    
    def generate_configs(self):
        Tools.run_shell_command("sudo {0}/generateconfigs.sh".format(shell_path))
        self.read_addresses()
        return

    def read_addresses(self):
        all_addresses_path = "{0}/allAddress.json".format(testnet_builder_data_path)
        witnesses_addresses_path = "{0}/witnessAddress.json".format(testnet_builder_data_path)

        self.all_addresses = Tools.read_file_to_json(all_addresses_path)
        self.witness_addresses = Tools.read_file_to_json(witnesses_addresses_path)
        self.headless_addresses = list(set(self.all_addresses).difference(set(self.witness_addresses)))

        self.first_utxo = self.headless_addresses[0]
        self.from_address = self.headless_addresses[1]
        self.payee_address = self.headless_addresses[2]

        return

    def setup_create_genesis(self):
        self.generate_configs()

        modify_dictionary = {
        "require('trustnote-headless')" : "require('../start')", 
        "require(\"trustnote-headless\")" : "require(\"../start\")", 
        old_first_utxo : self.first_utxo,
        old_from_address : self.from_address,
        old_payee_address : self.payee_address
        }

        path = "{0}/create_genesis.js".format(trustnote_headless_play_path)
        lines = Tools.read_file_to_lines(path)

        for index in range(len(lines)):
            for key in modify_dictionary.keys():
                if modify_dictionary[key] in lines[index]:
                    lines[index] = lines[index].replace(key, modify_dictionary[key])
                    Tools.log("Changed value from:{0} to :{1}".format(key, modify_dictionary[key]))

        #index = 0
        #while (index < len(lines)):
        #    if "require('trustnote-headless')" in lines[index].replace("\"", "'"):
        #        lines[index] = lines[index].replace("trustnote-headless", "../start")
        #    elif old_first_utxo in lines[index]:
        #        lines[index] = lines[index].replace(old_first_utxo, self.first_utxo)
        #        Tools.log("changed old_first_utxo:{0} to new first_utxo:{1}".format(old_first_utxo, self.first_utxo))
        #    elif old_from_address in lines[index]:
        #        lines[index] = lines[index].replace(old_from_address, self.from_address)
        #        Tools.log("changed old_from_address:{0} to new from_address:{1}".format(old_from_address, self.from_address))
        #    elif old_payee_address in lines[index]:
        #        lines[index] = lines[index].replace(old_payee_address, self.payee_address)
        #        Tools.log("changed old_payee_address:{0} to new payee_address:{1}".format(old_payee_address, self.payee_address))
        #    index = index + 1

        Tools.write_file_in_lines(path, lines)

        return

    def create_genesis(self):
        self.setup_create_genesis()

        Tools.run_shell_cd(trustnote_headless_play_path)
        output = Tools.run_shell_command_with_output("node create_genesis.js")
        Tools.run_shell_cd(home_path)
        Tools.log(output)

        return
   
try:
    main_chain_setter = MainChainSetter()
    #main_chain_setter.setup_os_env()
    #main_chain_setter.load_code()
    #main_chain_setter.create_genesis()
    main_chain_setter.setup_create_genesis()
    
except Exception as error:
    Tools.log(error)
    
