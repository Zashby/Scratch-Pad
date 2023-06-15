import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        try:
            del self.connections[connection_id]
            return "complete"
        except:
            print("Connection does not exist")

    def load(self):
        """Calculates the current load for all connections."""
        total = sum(x for x in self.connections.values())
        # Add up the load for each of the connections

        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


server = Server()
server.add_connection("192.168.1.1")

print(server.connections)
print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        self.connections[connection_id].close_connection(connection_id)
        # Close the connection on the server
        # Remove the connection from the load balancer
        del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        avgLoad = 0
        for server in self.servers:
            avgLoad += server.load()
        return avgLoad/len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >= 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

# Add a new server
l.servers.append(Server())
print(l.avg_load())

# Delete connection
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())
