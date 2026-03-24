class Router:
    _instance=None
    def __new__(cls,ssid="DefualtSSID",password="default123"):
        cls.list=[]
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.ssid=ssid
            cls._instance.password=password
            print(f"Router created with SSID: {cls._instance.ssid}")
        return cls._instance
    
    def connect_device(self,device_name):
        if device_name in self.list:
            print(f"Device {device_name} is already connected to SSID {self.ssid}")
            return
        self.list.append(device_name)
        print(f"Device {device_name} connected to SSID {self.ssid}")
    
    def show_connected_devices(self):
        print(f"Devices connected to {self.ssid}:")
        i=1
        for item in self.list:
            print(f:<100"{i}. {item}")
            i+=1
