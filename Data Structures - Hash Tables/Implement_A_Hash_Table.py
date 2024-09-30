class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size  # [None, None, None, None, ...]

    def _hash(self, key):  # Turn a 'key' word into a single number index for the Hash Table | Produces the address for the 'value'
        hash = 0
        for i in range(len(key)):  # For loop that goes from 0 to numerical length of key
            hash = (hash + ord(key[i]) * i) % self.size  # ord(key[i]) => number version of a specific character at a given index | A number that fit within the Data Structures - Hash Tables index / size boundaries
        return hash  # Returns a single number

    def set(self, key, value):
        address = self._hash(key)  # Produce the address / index of the home for the future key/value pair
        if not self.data[address]:  # Check if the location in the Hash Table is not occupied by data | Check for an empty lot at the given index / address | If no data is there
            self.data[address] = [[key, value]]  # Array within an array, inner array hold key/value pair, outer array is for holding other key/value pairs at the same index / memory location
        else:  # If data is already at the location
            self.data[address].append([key, value])  # Add key/value pair data as an extension | Add a small array to the bigger array already there

        print(self.data)

    def get(self, key):
        address = self._hash(key)  # Turn the key into the address where it should be on the Hash Table
        if self.data[address]:  # If the address location is full of data
            for keyValuePair in range(len(self.data[address])):  # For loop that goes through all key/value pair units at the given location
                if self.data[address][keyValuePair][0] == key:  # If the first element (key) of the key/value pair at the given Hash Table memory address matches the key we're searching for
                    return self.data[address][keyValuePair][1]  # Return the pair's second element (value
        return None  # Return None if key doesn't exist

    def allKeys(self):
        keysArray = []  # To store all Hash Table keys
        for address in range(self.size):  # Go through all the lots in the Hash Table
            if self.data[address]:  # If a data lot is filled
                if len(self.data[address]) > 1:  # If there is more than one data unit on the lot
                    for keyValuePair in range(len(self.data[address])):  # For every kay/value pair on the lot
                        keysArray.append(self.data[address][keyValuePair][0])  # Get key from key/value pair on the given memory lot
                else:  # Only one unit on the lot
                    keysArray.append(self.data[address][0][0])  # Get first element of first key/value pair at location
        return keysArray

    def allValues(self):
        valuesArray = []  # To store all Hash Table values
        for address in range(self.size):  # Go through all the lots in the Hash Table
            if self.data[address]:  # If a data lot is filled
                if len(self.data[address]) > 1:  # If there is more than one data unit on the lot
                    for keyValuePair in range(len(self.data[address])):  # For every kay/value pair on the lot
                        valuesArray.append(self.data[address][keyValuePair][1])  # Get value from key/value pair on the given memory lot
                else:  # Only one unit on the lot
                    valuesArray.append(self.data[address][0][1])  # Get second element of first key/value pair at location
        return valuesArray


newHT = HashTable(10)
newHT.set('Sony', 'PlayStation')
newHT.set('Microsoft', 'XBox')
newHT.set('Nintendo', 'Switch')
print(f"Keys: {newHT.allKeys()}")
print(f"Values: {newHT.allValues()}")


