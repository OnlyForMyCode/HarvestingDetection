from opcua import Client




class BulbHandler(object):
    def datachange_notification(self,node,val,data):
        print("New state: "+str(val))
        if val == True:
            print("Bulb is On")
        else:
            print("Bulb is off")



# Connect to server
client = Client("opc.tcp://127.0.0.1:123")
try:
    client.connect()
except:
    print("Could not connect to server")
else:
    bulb_var = client.get_node("ns=1;s=detection_state")
    
    handler = BulbHandler()

    sub = client.create_subscription(500,handler)
    handle = sub.subscribe_data_change(bulb_var)
    