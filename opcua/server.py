from time import sleep
from opcua import Server

server = Server()
server.set_endpoint("opc.tcp://127.0.0.1:123")
server.register_namespace("Room1")

objects = server.get_objects_node()
bulb = objects.add_variable("ns=6;s=DetectionState","detection_state",False)
bulb.set_writable()
marigold_coords = objects.add_variable("ns=6;s=::AsGlobalPV:FlowerPositions.Positions","coord_data",[""])
marigold_coords.set_writable()


try:
    print("Start Server")
    server.start()
    print("Server Online")
    while True:
        print("Detection State: "+str(bulb.get_value()))
        print("Coord Data: "+str(marigold_coords.get_value()))
        sleep(2)
        
finally:
    server.stop()
    print("Server Offline")