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
        conn_password=str(input("Enter password: "))
        if conn_password != self.password:
            raise ValueError("Incorrect password! connection failed")
        self.list.append(device_name)
        print(f"Device {device_name} connected to SSID {self.ssid}")
    
    def show_connected_devices(self):
        print('-'*40)
        print(f"Devices connected to {self.ssid}:")
        i=1
        for item in self.list:
            line=f"{i}. {item}"
            print(f"{' '*25}{line}")
            i+=1
        print('-'*40)

        
    def change_ssid(self):
        new_ssid=str(input("Enter new SSID: "))
        pass_word=str(input("Enter password to change SSID: "))
        if pass_word !=self.password:
            raise ValueError("Incorrect password! SSID change failed")
        self.ssid=new_ssid
        print("SSID Changed successfully")
    
    def update_password(self):
        old_password=str(input("Enter old password: "))
        if old_password != self.password:
            raise ValueError("Incorrect password! Password update failed")
        new_password=str(input("Enter new password: "))
        confirm_password=str(input("Enter confirm password: "))
        if new_password != confirm_password:
            raise ValueError("Passwords didn't match!")
        self.update_password=new_password
        print("Password updated successfully..")

router1=Router("FiberNet","Nepal123")



