from feats import Router
router1=Router("FiberNet","Nep@L57")
router1.connect_device("Honor 300 Lite")
router1.connect_device("Samsung S23 Ultra")
router1.connect_device("Iphone 17 Pro")
router1.connect_device("Iphone 17 Pro")
router1.connect_device("ZenBook 14")
try:
    router1.change_ssid()
except ValueError as e:
    print("Error: ",e)

try:
    router1.update_password()
except ValueError as e:
    print("Error: ",e)
    
router1.show_connected_devices()