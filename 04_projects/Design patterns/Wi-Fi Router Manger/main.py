from feats import Router
router1=Router("FiberNet","Nepal123")
devices=["Honor 300 Lite","Samsung S23 Ultra","Iphone 17 Pro","Iphone 17 Pro","ZenBook 14"]
for d in devices:
    try:
        router1.connect_device(d)
    except ValueError as e:
        print("Error: ",e)
try:
    router1.change_ssid()
    router1.update_password()
except ValueError as e:
    print("Error: ",e)

router1.show_connected_devices()