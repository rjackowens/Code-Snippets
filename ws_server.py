import asyncio
import websockets
import time
import random
import json


async def start_server(websocket, port):
    """
    start websocket server for testing

    args:
        websocket (str): server name
        port: (int): port to bind to

    """

    test_info = await websocket.recv()
    print(f"Received: {test_info}")

    loaded_test = json.loads(test_info)
    test_name = loaded_test["Name"]

    print(f"Running Test {test_name}")
    time.sleep(random.randrange(5, 15)) # simulate test run

    if test_name == 97:
        test_result = "Success"
    else:
        test_result = "Failure"

    test_results = {
        "Name": test_name,
        "Status": "Completed",
        "Result": test_result
    }

    json_test_results = json.dumps(test_results, indent=2)   

    await websocket.send(json_test_results)
    print(f"Sent: {json_test_results}")

print("Starting Server...")
start_server = websockets.serve(start_server, "localhost", 8765)
print("Server is up... ")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
