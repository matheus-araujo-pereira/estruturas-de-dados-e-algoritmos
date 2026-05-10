import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

array_vals = [3, 5, 13, 2]
array_cells = [(0, 1), (0, 2), (0, 3), (0, 4)]
ll_cells = [(1, 0), (3, 5), (2, 2), (1, 4)]


def memory_simulation():
    yield "array_alloc", -1, None, None
    yield "ll_alloc", -1, None, None
    for i in range(4):
        yield "array_trav", i, array_cells[i], None
    for i in range(4):
        next_cell = ll_cells[i + 1] if i < 3 else None
        yield "ll_trav", i, ll_cells[i], next_cell
    yield "end", -1, None, None


fig, ax = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title("Visualizador DSA")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.5, 4.5)

rects = {}
labels = {}

for r in range(4):
    for c in range(6):
        y = 3 - r
        x = c
        rect = plt.Rectangle(
            (x, y), 0.9, 0.9, facecolor="#F8F9FA", edgecolor="#DEE2E6", lw=1
        )
        ax.add_patch(rect)
        rects[(r, c)] = rect

        lbl = ax.text(
            x + 0.45,
            y + 0.45,
            "",
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            color="white",
        )
        labels[(r, c)] = lbl

arrows = []
for i in range(3):
    start = ll_cells[i]
    end = ll_cells[i + 1]

    start_x = start[1] + 0.45
    start_y = 3 - start[0] + 0.45
    end_x = end[1] + 0.45
    end_y = 3 - end[0] + 0.45

    arrow = ax.annotate(
        "",
        xy=(end_x, end_y),
        xytext=(start_x, start_y),
        arrowprops=dict(arrowstyle="->", color="#E94E77", lw=2.5),
        visible=False,
    )
    arrows.append(arrow)

texto_status = ax.text(
    3,
    4.3,
    "Inicializando Memória...",
    ha="center",
    fontsize=14,
    fontweight="bold",
    color="#333333",
)


def atualizar(frame):
    fase, idx, curr_cell, next_cell = frame

    for r in range(4):
        for c in range(6):
            rects[(r, c)].set_facecolor("#F8F9FA")
            labels[(r, c)].set_text("")

    if fase != "init":
        for i, cell in enumerate(array_cells):
            rects[cell].set_facecolor("#4A90E2")
            labels[cell].set_text(str(array_vals[i]))

    if fase not in ["init", "array_alloc"]:
        for i, cell in enumerate(ll_cells):
            rects[cell].set_facecolor("#A0B0C0")
            labels[cell].set_text(str(array_vals[i]))
        for a in arrows:
            a.set_visible(True)

    if fase == "array_alloc":
        texto_status.set_text("Array: Memória Contígua (blocos sequenciais)")
    elif fase == "ll_alloc":
        texto_status.set_text("Linked List: Memória Dispersa (conectada por ponteiros)")
    elif fase == "array_trav":
        rects[curr_cell].set_facecolor("#F5A623")
        texto_status.set_text(f"Array: Acessando índice {idx} (leitura linear)")
    elif fase == "ll_trav":
        rects[curr_cell].set_facecolor("#F5A623")
        if next_cell:
            texto_status.set_text(
                f"Linked List: Lendo nó {idx} -> Saltando pelo ponteiro"
            )
        else:
            texto_status.set_text(f"Linked List: Lendo nó {idx} -> Ponteiro null (Fim)")
    elif fase == "end":
        for cell in array_cells:
            rects[cell].set_facecolor("#50E3C2")
        for cell in ll_cells:
            rects[cell].set_facecolor("#50E3C2")
        texto_status.set_text("COMPARAÇÃO CONCLUÍDA: Arrays vs Linked Lists na Memória")

    return list(rects.values()) + list(labels.values()) + arrows + [texto_status]


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=memory_simulation(),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
