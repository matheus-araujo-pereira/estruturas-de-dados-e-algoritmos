import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [7, 12, 9, 4, 11, 5, 3, 8, 6, 10, 2, 1, 15, 14, 13, 16, 20, 18, 17, 19]


def buscar_menor(arr):
    min_idx = 0
    yield 0, min_idx

    for i in range(len(arr)):
        yield i, min_idx

        if arr[i] < arr[min_idx]:
            min_idx = i
            yield i, min_idx

    yield -1, min_idx


fig, ax = plt.subplots(figsize=(8, 5))
fig.canvas.manager.set_window_title("Visualizador DSA")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.tick_params(bottom=False)

barras = ax.bar(range(len(meu_array)), meu_array, color="#4A90E2")

ax.bar_label(barras, padding=3, fontsize=12)

texto_status = ax.text(
    0.5, 1.05, "", transform=ax.transAxes, ha="center", fontsize=14, fontweight="bold"
)


def atualizar(frame):
    idx_atual, idx_menor = frame

    for i, barra in enumerate(barras):
        barra.set_color("#4A90E2")

    barras[idx_menor].set_color("#E94E77")

    if idx_atual != -1:
        if idx_atual != idx_menor:
            barras[idx_atual].set_color("#F5A623")

        texto_status.set_text(
            f"Inspecionando: {meu_array[idx_atual]}  |  Menor registrado: {meu_array[idx_menor]}"
        )
    else:
        texto_status.set_text(
            f"BUSCA CONCLUÍDA! O menor valor é: {meu_array[idx_menor]}"
        )

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=buscar_menor(meu_array),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
