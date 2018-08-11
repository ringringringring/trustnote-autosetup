import os
import json
import platform
import subprocess

class Tools:
    """common tool functions."""

    def __init__(self):
        return

    @staticmethod
    def run_shell_command(command):
        Tools.log("command: {0}".format(command))
        os.system(command)
    
    @staticmethod
    def run_shell_command_with_output(command):
        result = subprocess.run(command, stdout=subprocess.PIPE)
        Tools.log("command: {0}".format(command))
        return result.stdout.decode('utf-8')

    @staticmethod
    def run_shell_cd(path):
        Tools.log("command: cd {0}".format(path))
        os.chdir(path)

    @staticmethod
    def log(message):
        print(message)

    @staticmethod
    def read_file(path):
        text = ""
        with open(path) as content:
             text = content

        return text

    @staticmethod
    def read_file_to_json(path):
        text = []
        with open(path) as content:
             text = json.load(content)

        return text

    @staticmethod
    def read_file_to_lines(path):
        lines = []
        with open(path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def write_file_in_lines(path, lines):
        with open(path, 'w', encoding='UTF-8') as f:
            f.writelines(lines)
    
    @staticmethod
    def current_paltform():
        platform_value = platform.platform()
        if ( "Windows" in platform_value ):
            return "Windows"
        elif ( "Linux" in platform_value ):
            return "Linux"
        else:
            return "Unkown"

    @staticmethod
    def cross_platfrom_path(path):
        platform_value = Tools.current_paltform()
        if ( platform_value != "Windows" ):
            return path.replace("\\", "/")
        
        return path.replace("/", "\\")