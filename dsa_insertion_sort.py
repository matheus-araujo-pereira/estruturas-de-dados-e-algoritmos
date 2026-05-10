import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [
    64,
    34,
    25,
    12,
    22,
    11,
    90,
    45,
    78,
    56,
    23,
    67,
    89,
    10,
    5,
    3,
    1,
    0,
    99,
    88,
    77,
]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        yield arr, i, -1, insert_index, current_value, False

        j = i - 1
        while j >= 0 and arr[j] > current_value:
            yield arr, i, j, insert_index, current_value, False
            arr[j + 1] = arr[j]
            insert_index = j
            yield arr, i, j, insert_index, current_value, False
            j -= 1

        arr[insert_index] = current_value
        yield arr, i, -1, insert_index, current_value, False

    yield arr, -1, -1, -1, -1, True


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
    arr, idx_i, idx_j, insert_idx, current_val, finalizado = frame

    for k, barra in enumerate(barras):
        barra.set_height(arr[k])
        rotulos[k].set_text(str(arr[k]))
        if k <= idx_i:
            barra.set_color("#50E3C2")
        else:
            barra.set_color("#4A90E2")

    if finalizado:
        for barra in barras:
            barra.set_color("#50E3C2")
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    if idx_j != -1:
        barras[idx_j].set_color("#F5A623")
        texto_status.set_text(f"Avaliando índice {idx_j} | Valor na mão: {current_val}")
    else:
        texto_status.set_text(f"Posicionando o valor {current_val}")

    barras[insert_idx].set_color("#E94E77")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=insertion_sort(meu_array.copy()),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
