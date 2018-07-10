from pymongo import MongoClient

settings = {
    "ip":'127.0.0.1',   #ip
    "port":27017,           #端口
    "db_name" : "deveops",    #数据库名字
    "set_name" : "asset"   #集合名字
}


class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self,dic):
        print("inser...")
        self.my_set.insert(dic)

    def update(self,dic,newdic):
        print("update...")
        self.my_set.update(dic,newdic)

    def delete(self,dic):
        print("delete...")
        self.my_set.remove(dic)

    def dbfind(self,dic,limit,search):
        print("find...")
        data = self.my_set.find(dic)
        callback = []

        for result in data:
            callback.append(
                {
                    "id":result.get("_id",None),
                    "hostname":result.get("hostname",None),
                    "management_ip":result.get("management_ip",None),
                    "server_ip": result.get("management_ip", None),
                    "admin_name":result.get("admin_name",None),
                    "asset_type":result.get("asset_type",None)
                }

            )
        print("Mongodb",callback)

        return callback