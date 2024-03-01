import queue
import random
import time

queue = queue.Queue()
client_id_counter = 1

def generate_request():

    global client_id_counter
    client_id = client_id_counter
    client_id_counter += 1

    operations = random.randint(1, 3)
    queue.put((client_id, operations))

    print(f"\nNew client {client_id} with {operations} operations added to the queue.")
    

def process_request():

    if not queue.empty():

        client_id, operations = queue.get()
        print(f"\nCurrent client {client_id} with {operations} operations")

        for operation in range(operations):
            print(f"\nOperation {operation + 1} for client with ID {client_id}")
            time.sleep(2)

    else:
        return "Queue is empty!"

while True:

    exit_word = input("\nInput 'exit' for break or press 'Enter': ")

    if exit_word == "exit":

        print("You did a good job today!")
        break

    generate_request()
    process_request()