from macchanger import MACCHANGER

if __name__=="__main__":
    mc=MACCHANGER()
    mac=mc.get_Mac("wlan0")
    print(mac)

    current_mac=mc.change_mac("wlan0","00:22:54:66:87:99")
    print(current_mac)
#for fun
