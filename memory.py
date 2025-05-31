# memory.py

# A simple dictionary to act as shared memory
shared_memory = {}

# Function to store data in shared memory
def store_data(key, value):
    shared_memory[key] = value

# Function to retrieve data from shared memory
def get_data(key):
    return shared_memory.get(key)