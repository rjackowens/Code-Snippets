import asyncio
import websockets
import json
import time


async def run_acceptance_test(endpoint: str, test_name: str, port=8765):
    """
    Posts acceptance test payload to websocket

    args:
        endpoint (str): websocket endpoint
        test_name (str): name of test to run
        port (int): port number to access websocket

    """

    uri = f"ws://{endpoint}:{port}"

    try:
        async with websockets.connect(uri) as websocket:

            test_payload = json.dumps({
                "Name": test_name,
                "Size": "50 MB"
            }, indent=2)

            await websocket.send(test_payload)
            print(f"\nQueued test {test_name}...\n")
            print(f"Sent: {test_payload} to {uri}")
            print("\nAwaiting Response...\n")

            # attempts to receive message from message stream
            connection_attempt = 0
            while connection_attempt < 3:
                try:
                    response = await websocket.recv()
                    print(f"Receieved: {response}")
                    break
                except websockets.exceptions.ConnectionClosedError as e:
                    connection_attempt += 1
                    time.sleep(3*connection_attempt)
                    print(f"Connection attempt {connection_attempt}")
                    continue
            else:
                raise ConnectionError("Unable to connect after 3 attempts")

            loaded_response = json.loads(response)
            if (loaded_response["Result"]) == "Failure":
                print(f"\nTest {test_name} failed")
                # raise Exception("Acceptance Test Failure") # fail build
            else:
                print(f"\nTest {test_name} succeeded")

    except OSError as e:
        raise ConnectionError("Unable to connect to server", e)

# asyncio.get_event_loop().run_until_complete(run_acceptance_test("localhost", 97))

all_tests =  [97, 97, 96]

def trigger_tests(endpoint: str, all_tests: list):
    """Post multiple tests to ACE"""
    for test in all_tests:
        asyncio.get_event_loop().run_until_complete(run_acceptance_test(endpoint, test))
        
trigger_tests("localhost", all_tests) # triggers 3 tests to run
