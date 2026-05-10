import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [7, 12, 9, 4, 11, 5, 3, 8, 6, 10, 2, 1, 15, 14, 13, 16, 20, 18, 17, 19]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        yield list(arr), "comparando", k, l, r, False
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        yield list(arr), "mesclando", k, l, r, False
        k += 1

    while i < n1:
        arr[k] = L[i]
        yield list(arr), "mesclando", k, l, r, False
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        yield list(arr), "mesclando", k, l, r, False
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m + 1, r)
        yield from merge(arr, l, m, r)


def merge_sort_generator(arr):
    yield from merge_sort(arr, 0, len(arr) - 1)
    yield list(arr), "fim", -1, -1, -1, True


fig, ax = plt.subplots(figsize=(12, 6))
fig.canvas.manager.set_window_title("Visualizador DSA")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.get_yaxis().set_visible(False)
ax.tick_params(bottom=False)

barras = ax.bar(range(len(meu_array)), meu_array, color="#4A90E2")
rotulos = ax.bar_label(barras, padding=3, fontsize=10)

texto_status = ax.text(
    0.5, 1.05, "", transform=ax.transAxes, ha="center", fontsize=14, fontweight="bold"
)


def atualizar(frame):
    arr, fase, idx, left_bound, right_bound, finalizado = frame

    for k, barra in enumerate(barras):
        barra.set_height(arr[k])
        rotulos[k].set_text(str(arr[k]))

        if left_bound <= k <= right_bound:
            barra.set_color("#4A90E2")
        else:
            barra.set_color("#B9D3F9")

    if finalizado:
        for barra in barras:
            barra.set_color("#50E3C2")
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    if fase == "comparando":
        barras[idx].set_color("#F5A623")
        texto_status.set_text(
            f"Avaliando bloco do índice {left_bound} ao {right_bound}"
        )
    elif fase == "mesclando":
        barras[idx].set_color("#E94E77")
        texto_status.set_text(f"Mesclando ordenado no índice {idx}")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=merge_sort_generator(meu_array.copy()),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
