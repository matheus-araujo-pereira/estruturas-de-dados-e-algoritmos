import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4


def traverse_linked_list(head):
    current = head
    idx = 0
    while current is not None:
        yield current, idx, False
        current = current.next
        idx += 1
    yield None, -1, True


fig, ax = plt.subplots(figsize=(10, 4))
fig.canvas.manager.set_window_title("Visualizador DSA")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.set_xlim(-1, 10)
ax.set_ylim(-2, 2)

nodes_vals = [3, 5, 13, 2]
x_coords = [0, 2.5, 5, 7.5]

circles = []

for i, val in enumerate(nodes_vals):
    circle = plt.Circle((x_coords[i], 0), 0.6, color="#4A90E2", zorder=3)
    ax.add_patch(circle)
    circles.append(circle)

    ax.text(
        x_coords[i],
        0,
        str(val),
        color="white",
        fontsize=14,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )

    if i < len(nodes_vals) - 1:
        ax.annotate(
            "",
            xy=(x_coords[i + 1] - 0.6, 0),
            xytext=(x_coords[i] + 0.6, 0),
            arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
        )

ax.text(
    x_coords[-1] + 1.8,
    0,
    "null",
    fontsize=14,
    color="#A0B0C0",
    ha="center",
    va="center",
)
ax.annotate(
    "",
    xy=(x_coords[-1] + 1.2, 0),
    xytext=(x_coords[-1] + 0.6, 0),
    arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
)

texto_status = ax.text(
    4.5, 1.3, "", ha="center", fontsize=14, fontweight="bold", color="#333333"
)

pointer = ax.annotate(
    "current",
    xy=(x_coords[0], -0.7),
    xytext=(x_coords[0], -1.5),
    arrowprops=dict(facecolor="#F5A623", edgecolor="none", shrink=0.05),
    fontsize=12,
    color="#F5A623",
    ha="center",
    va="top",
)


def atualizar(frame):
    current_node, idx, finalizado = frame

    for c in circles:
        c.set_color("#4A90E2")

    if finalizado:
        for c in circles:
            c.set_color("#50E3C2")
        texto_status.set_text("TRAVESSIA CONCLUÍDA! Ponteiro chegou ao null.")
        pointer.set_visible(False)
        return circles

    if idx != -1:
        circles[idx].set_color("#F5A623")
        pointer.xy = (x_coords[idx], -0.7)
        pointer.set_position((x_coords[idx], -1.5))
        pointer.set_visible(True)

        proximo = current_node.next.data if current_node.next else "null"
        texto_status.set_text(
            f"Lendo nó: {current_node.data} | Próximo aponta para: {proximo}"
        )

    return circles


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=traverse_linked_list(node1),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
