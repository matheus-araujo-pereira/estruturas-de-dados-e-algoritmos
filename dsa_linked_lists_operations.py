import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def operacoes_simulacao():
    # 1. Traversing (Travessia)
    for i in range(4):
        yield "trav", i, -1, "Percorrendo a lista (Traversing)"

    # 2. Deleting (Exclusão do Nó 'C')
    yield "del", 2, -1, "Excluindo o nó 'C': Ponteiro de 'B' pula para 'D'"

    # 3. Inserting (Inserção de 'E' entre 'A' e 'B')
    yield "ins", 0, 1, "Inserindo 'E': 'A' aponta para 'E', e 'E' aponta para 'B'"


fig, ax = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title("Visualizador DSA - Operações em Listas")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 4)

nodes_info = [
    {"id": "A", "x": 1},
    {"id": "B", "x": 3},
    {"id": "C", "x": 5},
    {"id": "D", "x": 7},
]
y_pos = 1

circles = {}
labels = {}
for n in nodes_info:
    c = plt.Circle((n["x"], y_pos), 0.45, color="#4A90E2", zorder=3)
    ax.add_patch(c)
    circles[n["id"]] = c
    l = ax.text(
        n["x"],
        y_pos,
        n["id"],
        color="white",
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )
    labels[n["id"]] = l

# Nó E para inserção posterior
circle_e = plt.Circle((2, -0.5), 0.45, color="#50E3C2", zorder=3, visible=False)
ax.add_patch(circle_e)
label_e = ax.text(
    2,
    -0.5,
    "E",
    color="white",
    fontsize=12,
    fontweight="bold",
    ha="center",
    va="center",
    zorder=4,
    visible=False,
)

# Setas iniciais
setas = {
    "AB": ax.annotate(
        "",
        xy=(2.55, y_pos),
        xytext=(1.45, y_pos),
        arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
    ),
    "BC": ax.annotate(
        "",
        xy=(4.55, y_pos),
        xytext=(3.45, y_pos),
        arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
    ),
    "CD": ax.annotate(
        "",
        xy=(6.55, y_pos),
        xytext=(5.45, y_pos),
        arrowprops=dict(arrowstyle="->", color="#A0B0C0", lw=2),
    ),
}

# Setas especiais para operações
seta_bd = ax.annotate(
    "",
    xy=(6.55, y_pos + 0.2),
    xytext=(3.45, y_pos + 0.2),
    arrowprops=dict(
        arrowstyle="->", color="#E94E77", lw=2, connectionstyle="arc3,rad=-0.3"
    ),
    visible=False,
)
seta_ae = ax.annotate(
    "",
    xy=(2, -0.05),
    xytext=(1, 0.55),
    arrowprops=dict(arrowstyle="->", color="#50E3C2", lw=2),
    visible=False,
)
seta_eb = ax.annotate(
    "",
    xy=(3, 0.55),
    xytext=(2, -0.05),
    arrowprops=dict(arrowstyle="->", color="#50E3C2", lw=2),
    visible=False,
)

texto_status = ax.text(4, 3, "", ha="center", fontsize=14, fontweight="bold")


def atualizar(frame):
    fase, idx1, idx2, msg = frame
    texto_status.set_text(msg)

    # Reset
    for c in circles.values():
        c.set_color("#4A90E2")
    circle_e.set_visible(False)
    label_e.set_visible(False)
    seta_bd.set_visible(False)
    seta_ae.set_visible(False)
    seta_eb.set_visible(False)
    for s in setas.values():
        s.set_visible(True)

    if fase == "trav":
        node_id = nodes_info[idx1]["id"]
        circles[node_id].set_color("#F5A623")

    elif fase == "del":
        circles["C"].set_color("#E94E77")
        setas["BC"].set_visible(False)
        setas["CD"].set_visible(False)
        seta_bd.set_visible(True)

    elif fase == "ins":
        circle_e.set_visible(True)
        label_e.set_visible(True)
        setas["AB"].set_visible(False)
        seta_ae.set_visible(True)
        seta_eb.set_visible(True)

    return (
        list(circles.values())
        + list(setas.values())
        + [circle_e, seta_bd, seta_ae, seta_eb, texto_status]
    )


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=operacoes_simulacao(),
    interval=500,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
