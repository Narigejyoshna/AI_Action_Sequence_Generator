import networkx as nx
import matplotlib.pyplot as plt


def visualize_plan(plan):
    G = nx.DiGraph()

    for i in range(len(plan)):
        G.add_node(plan[i])

        if i > 0:
            G.add_edge(plan[i - 1], plan[i])

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 5))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=3000,
        font_size=10,
        font_weight='bold',
        arrows=True
    )

    plt.title("Planning Graph Action Sequence")
    plt.show()