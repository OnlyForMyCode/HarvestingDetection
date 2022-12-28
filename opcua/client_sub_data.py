from opcua import Client

class DataHandler(object):
    def datachange_notification(self,node,val,data):
        print("New state: "+str(val))
client = Client("opc.tcp://127.0.0.1:123")
try:
    client.connect()
except:
    print("Could not connect to server")
else:
    coord_data = client.get_node("ns=6;s=::AsGlobalPV:FlowerPositions.Positions")
    handler = DataHandler()
    
    sub = client.create_subscription(500,handler)
    handle = sub.subscribe_data_change(coord_data)