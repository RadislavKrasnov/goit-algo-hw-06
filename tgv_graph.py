import networkx as nx
import matplotlib.pyplot as plt

def create_tgv_graph():
    tgv_graph = {
        'Paris': [
            'London', 
            'Bruxelles', 
            'Nantes', 
            'Rennes', 
            'La Rochelle', 
            'Lyon', 
            'Reims', 
            'Lille', 
            'Luxemburg', 
            'Strasbourge', 
            'Nancy',
            'Geneve',
            'Zurich',
            'Frankfurt',
            'Stuttgart',
            'Bordeaux'
        ],
        'Lyon': [
            'Saint-Etienne',
            'Marseille',
            'Geneve',
            'Paris',
            'Zurich',
            'Grenoble',
            'Montpellier'
        ],
        'Marseille': [
            'Nice',
            'Montpellier',
            'Lyon',
            'Grenoble',
        ],
        'Montpellier': [
            'Barcelona',
            'Marseille',
            'Grenoble',
            'Lyon'
        ],
        'Barcelona': [
            'Montpellier',
        ],
        'Nice': [
            'Marseille'
        ],
        'Grenoble': [
            'Milano',
            'Lyon'
        ],
        'Saint-Etienne': [
            'Lyon'
        ],
        'Milano': [
            'Grenoble'
        ],
        'Geneve': [
            'Paris',
            'Lyon',
            'Zurich'
        ],
        'Zurich': [
            'Paris',
            'Lyon',
            'Geneve'
        ],
        'Reims': [
            'Paris',
            'La Rochelle', 
            'Strasbourge', 
            'Nancy',
            'Frankfurt',
            'Stuttgart',
            'Luxemburg'
        ],
        'Luxemburg': [
            'Paris',
            'Reims',
            'Strasbourge',
            'Nancy',
            'Stuttgart',
            'Frankfurt'
        ],
        'Nancy': [
            'Luxemburg',
            'Reims',
            'Paris',
            'Frankfurt',
            'Stuttgart',
            'Strasbourge'
        ],
        'Frankfurt': [
            'Luxemburg',
            'Reims',
            'Paris',
            'Stuttgart',
            'Strasbourge',
            'Nancy'
        ],
        'Stuttgart': [
            'Luxemburg',
            'Reims',
            'Paris',
            'Strasbourge',
            'Nancy'
            'Frankfurt'
        ],
        'Strasbourge': [
            'Luxemburg',
            'Reims',
            'Paris',
            'Colmar',
            'Nancy'
            'Frankfurt',
            'Stuttgart'
        ],
        'Colmar': [
            'Strasbourge'
        ],
        'Lille': [
            'Paris',
            'London',
            'Bruxelles'
        ],
        'Bruxelles': [
            'Amsterdam',
            'Lille',
            'Paris',
            'London'
        ],
        'Amsterdam': [
            'Bruxelles'
        ],
        'Rennes': [
            'Paris',
            'Nantes',
            'La Rochelle',
            'Bordeaux',
            'Saint-Malo',
            'Quimper',
            'Brest',
        ],
        'Saint-Malo': [
            'Rennes',
            'Brest'
        ],
        'Brest': [
            'Rennes',
            'Saint-Malo'
        ],
        'Quimper': [
            'Rennes'
        ],
        'Nantes': [
            'Paris',
            'Bordeaux',
            'La Rochelle',
            'Rennes'
        ],
        'Bordeaux': [
            'Paris',
            'Nantes',
            'Rennes',
            'La Rochelle',
            'Hendaye',
            'Pau',
            'Toulouse',
        ],
        'Toulouse': [
            'Bordeaux',
            'Hendaye',
            'Pau',
        ],
        'Pau': [
            'Bordeaux',
            'Hendaye',
            'Toulouse',
        ],
        'Hendaye': [
            'Bordeaux',
            'Toulouse',
            'Pau',
        ]
    }

    return nx.Graph(tgv_graph)

def visualize_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()

def get_vertices_qty(G):
    return G.number_of_nodes()

def get_edges_qty(G):
    return G.number_of_edges()

def get_vertices_degrees(G):
    return G.degree()

G = create_tgv_graph()
print(f'Vertices quantity in the graph: {get_vertices_qty(G)}')
print(f'Edges quantity in the graph: {get_edges_qty(G)}')
for vertex in get_vertices_degrees(G):
    print(f'Vertex {vertex[0]} has degree {vertex[1]}')
visualize_graph(G)
