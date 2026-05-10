import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [11, 9, 29, 7, 2, 15, 28, 23, 4, 27, 1, 19, 8, 17, 3, 26, 5, 14, 10, 6]


def partition(arr, low, high, done_indices):
    pivot = arr[high]
    i = low - 1
    yield arr, low, high, high, i, -1, done_indices

    for j in range(low, high):
        yield arr, low, high, high, i, j, done_indices
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, low, high, high, i, j, done_indices

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr, low, high, i + 1, i + 1, -1, done_indices
    return i + 1


def quick_sort(arr, low, high, done_indices):
    if low < high:
        pi = yield from partition(arr, low, high, done_indices)
        done_indices.add(pi)
        yield arr, low, high, pi, -1, -1, done_indices

        yield from quick_sort(arr, low, pi - 1, done_indices)
        yield from quick_sort(arr, pi + 1, high, done_indices)
    elif low == high:
        done_indices.add(low)
        yield arr, low, high, -1, -1, -1, done_indices


def quick_sort_generator(arr):
    done_indices = set()
    yield from quick_sort(arr, 0, len(arr) - 1, done_indices)

    for i in range(len(arr)):
        done_indices.add(i)
    yield arr, -1, -1, -1, -1, -1, done_indices


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
    arr, low, high, pivot_idx, i_idx, j_idx, done_indices = frame

    for k, barra in enumerate(barras):
        barra.set_height(arr[k])
        rotulos[k].set_text(str(arr[k]))

        if k in done_indices:
            barra.set_color("#50E3C2")
        elif low <= k <= high:
            barra.set_color("#4A90E2")
        else:
            barra.set_color("#B9D3F9")

    if low == -1:
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    if pivot_idx != -1 and pivot_idx not in done_indices:
        barras[pivot_idx].set_color("#E94E77")

    if j_idx != -1:
        barras[j_idx].set_color("#F5A623")
        texto_status.set_text(f"Pivot: {arr[pivot_idx]} | Analisando: {arr[j_idx]}")
    else:
        texto_status.set_text(f"Particionando do índice {low} ao {high}")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=quick_sort_generator(meu_array.copy()),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
