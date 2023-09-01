import sys
import yara
from os import path,walk


class Scan:
    def __init__(self,directoryToScan:str,rules_path:str="",hash_list:str="") -> None:
        self.dirToScan= directoryToScan
        self.yaraRulePath = rules_path
        self.hashlistPath = hash_list

    def yara_scan(self)-> dict:
        
        if not path.exists(self.dirToScan):
            print("Invalid path provided")
            self.__exit__()
        
        rules = yara.compile(filepath=self.yaraRulePath)
        
        results = {}
        for root, _, files in walk(self.dirToScan, followlinks=False):
            for filename in files:
                current_file = path.join(root, filename)
                print("scanning ", path.abspath(current_file))
                matches = rules.match(current_file, fast=True, )
                if matches:
                    results[path.abspath(current_file)] = matches[0]
        return results
    
    def hash_scan(self) -> dict:
        global malware_hashes
        if not path.exists(self.dirToScan):
            print("invalid path")
            self.__exit__()
        
        files_to_be_checked = {}
        for root, _, files in walk(self.dirToScan, followlinks=False):
            for filename in files:
                current_file = path.join(root, filename)
                files_to_be_checked[path.abspath(current_file)] = self.convert_to_sha256(path.abspath(current_file))

        if not self.hashlistPath:
            try:
                pass
                # to do 
                # to create a db of hashes of virus of the latest
                # and add support for it here
            except:
                pass

        if self.hashlistPath:
            result = {}
            malware_hashes_list = list(open(self.hashlistPath, "r").read().split("\n"))
            for key in files_to_be_checked:
                if files_to_be_checked[key] in malware_hashes_list:
                    result[path.abspath(key)] = files_to_be_checked[key]
            return result 

    def __exit__():
        sys.exit()