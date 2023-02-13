from opcua import Client

client = Client("opc.tcp://127.0.0.1:4840")
client.connect()

objects = client.get_objects_node()

bulb_var = client.get_node("ns=6;s=DetectionState")
print(bulb_var.get_value())
coord_data = client.get_node("ns=6;s=::AsGlobalPV:FlowerPositions.Positions")
print(coord_data.get_value())
bulb_var.set_value(True)
#coord_data.set_value(["Hallo","Test","Test"])
client.disconnect()
