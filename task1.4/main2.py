import csv
import heapq  # Importing heapq module for priority queue implementation


def read_railway_network(filename):
    network = {}  # Initialize an empty dictionary to store the network data
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader object
        for row in reader:  # Iterate over each row in the CSV file
            start, end, cost = row  # Extract start station, end station, and cost from the row
            if start not in network:
                network[start] = {}  # If start station not in network, add it with an empty dictionary
            network[start][end] = int(cost)  # Add end station and cost to start station's dictionary
            if end not in network:
                network[end] = {}  # If end station not in network, add it with an empty dictionary
            network[end][start] = int(cost)  # connections can be bidirectional, add reverse connection
    return network  # Return the constructed network dictionary


def dijkstra(network, start, end):

    queue = [(0, start, [])]  # Priority queue to store (cost, current_node, path)
    visited = set()  # Set to keep track of visited nodes

    while queue:  # Continue until the queue is empty
        cost, current_node, path = heapq.heappop(queue)  # Pop the node with the lowest cost from the queue

        if current_node == end:  # If the current node is the destination
            path.append(end)  # Add destination to the path
            return cost, path  # Return the cost and the path

        if current_node not in visited:  # If the current node has not been visited yet
            visited.add(current_node)  # Mark the current node as visited
            path.append(current_node)  # Add the current node to the path

            for neighbor, neighbor_cost in network[current_node].items():  # Iterate over neighbors of current node
                if neighbor not in visited:  # If the neighbor has not been visited
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor, path[:]))  # Push neighbor to the queue

    return float('inf'), []  # Return infinity cost and an empty path if no route is found



def main():
    network = read_railway_network('task1_4_railway_network.csv')
    departure = input("Enter the departure station: ")
    destination = input("Enter the destination station: ")

    if departure not in network or destination not in network:
        print("Invalid input stations.")
        return

    cheapest_cost, route = dijkstra(network, departure, destination)
    if cheapest_cost == float('inf'):
        print("No route found between the stations.")
    else:
        print(f"The cheapest cost from {departure} to {destination} is {cheapest_cost}.")
        print("Route:")
        print(" -> ".join(route))


if __name__ == "__main__":
    main()