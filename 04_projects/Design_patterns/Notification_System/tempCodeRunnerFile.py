
        dt_format=dt.datetime.now().replace(microsecond=0).isoformat()
        def log(self,channel,message):
                with open("notification_log.txt","a") as f:
                    f.write(f"{dt.format} | {channel} | {message}\n")