# What is Network Analysis?

Network Analysis is a method used to explore and analyze the relationships and structures within networks, which consist of nodes (or vertices) and edges connecting them. It's widely used in various fields such as social science, biology, communication studies, and more. This analysis provides insights into how entities interact with each other within the network, identifies influential nodes, detects communities or clusters, and helps in understanding the overall structure and behavior of the network.

## Types of Business Questions Answered

Network Analysis can address diverse business and research questions, including:

- **Social Network Analysis:** Who are the key influencers within a social network?
- **Organizational Networks:** How do information and resources flow within an organization?
- **Market Analysis:** How do products or brands relate to each other in a market?
- **Supply Chain Analysis:** What are the critical points in a supply chain network?

## Types of Data Input

Network Analysis can be applied to data where relationships are key:

- **Social Networks:** Data about social interactions, connections, or relationships.
- **Biological Networks:** Such as genetic, protein-protein, or neural networks.
- **Transportation Networks:** Data about routes, trips, and connections in transportation systems.
- **Communication Networks:** Data from communication systems, like email networks.

## Useful Visuals and Metrics

Effective visuals and metrics for Network Analysis include:

- **Graph Visualizations:** Visual representation of the network.
- **Degree Centrality:** To identify the most connected nodes.
- **Betweenness Centrality:** To find nodes that serve as bridges within the network.
- **Community Detection Algorithms:** Like modularity, to detect clusters or communities within the network.

## Small Python Example

Here is a simple example using Python's NetworkX library for network analysis:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()

# Adding nodes and edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5)])

# Drawing the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

# Calculating degree centrality
centrality = nx.degree_centrality(G)
print(centrality)
```
