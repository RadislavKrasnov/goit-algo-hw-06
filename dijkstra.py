import networkx as nx
import matplotlib.pyplot as plt

def get_weighted_graph():
    return {
        'Paris': {
            'London': 2, 
            'Bruxelles': 1, 
            'Nantes': 2, 
            'Rennes': 1, 
            'La Rochelle': 3, 
            'Lyon': 2, 
            'Reims': 1, 
            'Lille': 1, 
            'Luxemburg': 2, 
            'Strasbourge': 2, 
            'Nancy': 2,
            'Geneve': 4,
            'Zurich': 5,
            'Frankfurt': 4,
            'Stuttgart': 3,
            'Bordeaux': 2,
        },
        'London': {
            'Paris': 2,
            'Lille': 2,
            'Bruxelles': 2,
        },
        'Lyon': {
            'Saint-Etienne': 1,
            'Marseille': 2,
            'Geneve': 2,
            'Paris': 2,
            'Zurich': 4,
            'Grenoble': 1,
            'Montpellier': 2,
        },
        'Marseille': {
            'Nice': 3,
            'Montpellier': 2,
            'Lyon': 2,
            'Grenoble': 3,
        },
        'Montpellier': {
            'Barcelona': 3,
            'Marseille': 2,
            'Grenoble': 3,
            'Lyon': 2,
        },
        'Barcelona': {
            'Montpellier': 3,
        },
        'Nice': {
            'Marseille': 3,
        },
        'Grenoble': {
            'Milano': 4,
            'Lyon': 1,
        },
        'Saint-Etienne': {
            'Lyon': 1,
        },
        'Milano': {
            'Grenoble': 4,
        },
        'Geneve': {
            'Paris': 4,
            'Lyon': 2,
            'Zurich': 3,
        },
        'Zurich': {
            'Paris': 5,
            'Lyon': 4,
            'Geneve': 3,
        },
        'Reims': {
            'Paris': 1,
            'Strasbourge': 2, 
            'Nancy': 2,
            'Frankfurt': 4,
            'Stuttgart': 3,
            'Luxemburg': 2,
        },
        'Luxemburg': {
            'Paris': 2,
            'Reims': 2,
            'Strasbourge': 2,
            'Nancy': 2,
            'Stuttgart': 3,
            'Frankfurt': 4,
        },
        'Nancy': {
            'Luxemburg': 2,
            'Reims': 2,
            'Paris': 2,
            'Frankfurt': 3,
            'Stuttgart': 3,
            'Strasbourge': 1,
        },
        'Frankfurt': {
            'Luxemburg': 4,
            'Reims': 4,
            'Paris': 4,
            'Stuttgart': 1,
            'Strasbourge': 2,
            'Nancy': 3,
        },
        'Stuttgart': {
            'Luxemburg': 3,
            'Reims': 3,
            'Paris': 3,
            'Strasbourge': 1,
            'Nancy': 3,
            'Frankfurt': 1,
        },
        'Strasbourge': {
            'Luxemburg': 2,
            'Reims': 2,
            'Paris': 2,
            'Colmar': 1,
            'Nancy': 1,
            'Frankfurt': 2,
            'Stuttgart': 1,
        },
        'Colmar': {
            'Strasbourge': 1,
        },
        'Lille': {
            'Paris': 1,
            'London': 2,
            'Bruxelles': 1,
        },
        'Bruxelles': {
            'Amsterdam': 2,
            'Lille': 1,
            'Paris': 1,
            'London': 2,
        },
        'Amsterdam': {
            'Bruxelles': 2,
        },
        'Rennes': {
            'Paris': 1,
            'Nantes': 1,
            'La Rochelle': 3,
            'Bordeaux': 4,
            'Saint-Malo': 1,
            'Quimper': 2,
            'Brest': 2,
        },
        'Saint-Malo': {
            'Rennes': 1,
            'Brest': 3,
        },
        'Brest': {
            'Rennes': 2,
            'Saint-Malo': 3,
        },
        'Quimper': {
            'Rennes': 2,
        },
        'Nantes': {
            'Paris': 2,
            'Bordeaux': 3,
            'La Rochelle': 2,
            'Rennes': 1,
        },
        'Bordeaux': {
            'Paris': 2,
            'Nantes': 3,
            'Rennes': 4,
            'La Rochelle': 2,
            'Hendaye': 3,
            'Pau': 2,
            'Toulouse': 2,
        },
        'La Rochelle': {
            'Bordeaux': 2,
            'Paris': 3,
            'Rennes': 3,
            'Nantes': 2,
        },
        'Toulouse': {
            'Bordeaux': 2,
            'Hendaye': 4,
            'Pau': 2,
        },
        'Pau': {
            'Bordeaux': 2,
            'Hendaye': 2,
            'Toulouse': 2,
        },
        'Hendaye': {
            'Bordeaux': 3,
            'Toulouse': 4,
            'Pau': 2,
        }
    }

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
    return distances

def print_shortest_paths(distances):
    print('Shortest paths to all destinations in the network of TGV rail roads for Marseille city:')
    for destination, time in distances.items():
        print(f'{destination} - {time} hours')

def visualize_weighted_graph(weighted_graph):
    G = nx.Graph()
    for vertex, destinations in weighted_graph.items():
        for neighbor_destination, travel_time in destinations.items():
            G.add_edge(vertex, neighbor_destination, weight=travel_time)
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos, node_size=300)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=2)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title('TGV travel time among cities of Europe')
    plt.show()

weighted_graph = get_weighted_graph()
distances = dijkstra(weighted_graph, 'Marseille')
print_shortest_paths(distances)
visualize_weighted_graph(weighted_graph)
