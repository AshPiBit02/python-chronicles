class DatabaseConnection:
    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.db_url=kwargs.get("db_url","sqlite://default")
            print(f"Connecting to {cls._instance.db_url}.....")
        _instance=None
        return cls._instance
    @classmethod
    def reset_instance(cls,db_url="sqlite://default"):
        cls._instance=None
        return cls(db_url=db_url)

# conn1=DatabaseConnection(db_url="mysql://localhost")
# conn2=DatabaseConnection(db_url="postgres://remote")
# print(conn1.db_url)
# print(conn2.db_url)