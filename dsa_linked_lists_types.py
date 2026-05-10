import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def tipos_listas_simulacao():
    # Estrutura: fase, highlighted_node_idx, highlight_color
    # 1. Singly Linked List (Unidirecional)
    for i in range(4):
        yield "singly", i, "#F5A623"

    # 2. Doubly Linked List (Bidirecional)
    for i in range(4):
        yield "doubly", i, "#F5A623"
    for i in range(3, -1, -1):
        yield "doubly", i, "#E94E77"

    # 3. Circular Linked List (Loop)
    for i in range(9):
        yield "circular", i % 4, "#50E3C2"


fig, ax = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title("Visualizador DSA - Tipos de Listas")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 5)

nodes_vals = ["A", "B", "C", "D"]
x_coords = [1, 3, 5, 7]
y_pos = 2

circles = []
for i, val in enumerate(nodes_vals):
    c = plt.Circle((x_coords[i], y_pos), 0.5, color="#4A90E2", zorder=3)
    ax.add_patch(c)
    circles.append(c)
    ax.text(
        x_coords[i],
        y_pos,
        val,
        color="white",
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )

setas_singly = []
for i in range(3):
    s = ax.annotate(
        "",
        xy=(x_coords[i + 1] - 0.5, y_pos),
        xytext=(x_coords[i] + 0.5, y_pos),
        arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
    )
    setas_singly.append(s)

setas_doubly_back = []
for i in range(3):
    s = ax.annotate(
        "",
        xy=(x_coords[i] + 0.5, y_pos - 0.2),
        xytext=(x_coords[i + 1] - 0.5, y_pos - 0.2),
        arrowprops=dict(arrowstyle="->", color="#E94E77", lw=2),
        visible=False,
    )
    setas_doubly_back.append(s)

seta_circular = ax.annotate(
    "",
    xy=(x_coords[0], y_pos + 0.5),
    xytext=(x_coords[3], y_pos + 0.5),
    arrowprops=dict(
        arrowstyle="->", color="#50E3C2", lw=2, connectionstyle="arc3,rad=-0.5"
    ),
    visible=False,
)

texto_status = ax.text(4, 4, "", ha="center", fontsize=14, fontweight="bold")
texto_tipo = ax.text(4, 0, "", ha="center", fontsize=12, color="#666666")


def atualizar(frame):
    fase, idx, cor = frame

    for c in circles:
        c.set_color("#4A90E2")

    circles[idx].set_color(cor)

    if fase == "singly":
        texto_status.set_text("Singly Linked List")
        texto_tipo.set_text("Navegação apenas para frente (Next)")
        for s in setas_doubly_back:
            s.set_visible(False)
        seta_circular.set_visible(False)

    elif fase == "doubly":
        texto_status.set_text("Doubly Linked List")
        texto_tipo.set_text("Navegação para frente (Next) e para trás (Prev)")
        for s in setas_doubly_back:
            s.set_visible(True)
        seta_circular.set_visible(False)

    elif fase == "circular":
        texto_status.set_text("Circular Linked List")
        texto_tipo.set_text("O último nó aponta de volta para o primeiro (Head)")
        for s in setas_doubly_back:
            s.set_visible(False)
        seta_circular.set_visible(True)

    return (
        circles
        + setas_singly
        + setas_doubly_back
        + [seta_circular, texto_status, texto_tipo]
    )


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=tipos_listas_simulacao(),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
