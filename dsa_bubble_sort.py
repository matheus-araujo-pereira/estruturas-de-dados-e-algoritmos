import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [64, 34, 25, 12, 22, 11, 90]


def bubble_sort_otimizado(arr):
    n = len(arr)
    for i in range(n - 1):
        houve_troca = False
        for j in range(n - i - 1):
            yield arr, j, j + 1, False, False

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                houve_troca = True
                yield arr, j, j + 1, True, False

        if not houve_troca:
            break

    yield arr, -1, -1, False, True


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
    arr, idx1, idx2, trocou, finalizado = frame

    for i, barra in enumerate(barras):
        barra.set_height(arr[i])
        barra.set_color("#4A90E2")
        rotulos[i].set_text(str(arr[i]))

    if finalizado:
        for barra in barras:
            barra.set_color("#50E3C2")
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    barras[idx1].set_color("#F5A623")
    barras[idx2].set_color("#F5A623")

    if trocou:
        barras[idx1].set_color("#E94E77")
        barras[idx2].set_color("#E94E77")
        texto_status.set_text(f"Trocando: {arr[idx2]} e {arr[idx1]}")
    else:
        texto_status.set_text(f"Comparando: {arr[idx1]} e {arr[idx2]}")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=bubble_sort_otimizado(meu_array.copy()),
    interval=800,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
