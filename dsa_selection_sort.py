import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [64, 25, 12, 22, 11, 5, 90, 45, 33, 27, 18, 2, 8, 19, 50, 40]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        yield arr, i, -1, min_idx, False, False

        for j in range(i + 1, n):
            yield arr, i, j, min_idx, False, False
            if arr[j] < arr[min_idx]:
                min_idx = j
                yield arr, i, j, min_idx, False, False

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, i, -1, min_idx, True, False

    yield arr, -1, -1, -1, False, True


fig, ax = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title("Visualizador DSA")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.tick_params(bottom=False)

barras = ax.bar(range(len(meu_array)), meu_array, color="#4A90E2")
rotulos = ax.bar_label(barras, padding=3, fontsize=12)

texto_status = ax.text(
    0.5, 1.05, "", transform=ax.transAxes, ha="center", fontsize=14, fontweight="bold"
)


def atualizar(frame):
    arr, idx_i, idx_j, min_idx, trocou, finalizado = frame

    for k, barra in enumerate(barras):
        barra.set_height(arr[k])
        rotulos[k].set_text(str(arr[k]))
        if k < idx_i:
            barra.set_color("#50E3C2")
        else:
            barra.set_color("#4A90E2")

    if finalizado:
        for barra in barras:
            barra.set_color("#50E3C2")
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    if not trocou:
        if idx_j != -1:
            barras[idx_j].set_color("#F5A623")
            texto_status.set_text(
                f"Procurando menor... Atual: {arr[idx_j]} | Menor: {arr[min_idx]}"
            )
        else:
            texto_status.set_text(f"Iniciando varredura a partir da posição {idx_i}")
        barras[min_idx].set_color("#E94E77")
    else:
        barras[idx_i].set_color("#E94E77")
        if idx_i != min_idx:
            barras[min_idx].set_color("#F5A623")
        texto_status.set_text(f"Movendo o {arr[idx_i]} para a posição ordenada")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=selection_sort(meu_array.copy()),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
