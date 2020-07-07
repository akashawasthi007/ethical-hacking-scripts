import subprocess
import re

class MACCHANGER:
    def _init_(self):
        self.MAC=""

    def get_Mac(self,iface):
        output=subprocess.run(["ifconfig",iface],shell=False,capture_output=True)
        cmd_result=output.stdout.decode('utf-8')
        #print(cmd_result)

        pattern=r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex=re.compile(pattern)
        ans=regex.search(cmd_result)
        current=ans.group().split(" ")[1]
        self.MAC=current
        return current

    def change_mac(self,iface,new_mac):
        print("current mac address id ",self.get_Mac(iface))
        output=subprocess.run(["ifconfig",iface,"down"],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))

        output=subprocess.run(["ifconfig",iface,"hw","ether",new_mac],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))

        output=subprocess.run(["ifconfig",iface,"up"],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))

        print("updated mac address ",self.get_Mac(iface))
        return self.get_Mac(iface)
