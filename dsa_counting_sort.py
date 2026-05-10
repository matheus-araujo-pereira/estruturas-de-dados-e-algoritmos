import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [7, 12, 9, 4, 11, 5, 3, 8, 6, 10, 2, 1, 15, 14, 13, 16, 20, 18, 17, 19]


def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    n = len(arr)

    for i in range(n):
        val = arr[i]
        count[val] += 1
        yield list(arr), "contando", i, val, False

    idx = 0
    for val in range(max_val + 1):
        while count[val] > 0:
            arr[idx] = val
            yield list(arr), "reconstruindo", idx, val, False
            idx += 1
            count[val] -= 1

    yield list(arr), "fim", -1, -1, True


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
    arr, fase, idx, val, finalizado = frame

    for k, barra in enumerate(barras):
        barra.set_height(arr[k])
        rotulos[k].set_text(str(arr[k]))

        if fase == "reconstruindo" and k < idx:
            barra.set_color("#50E3C2")
        else:
            barra.set_color("#4A90E2")

    if finalizado:
        for barra in barras:
            barra.set_color("#50E3C2")
        texto_status.set_text("ORDENAÇÃO CONCLUÍDA!")
        return barras

    if fase == "contando":
        barras[idx].set_color("#F5A623")
        texto_status.set_text(f"Fase 1: Contagem | Lendo o valor: {val}")
    elif fase == "reconstruindo":
        barras[idx].set_color("#E94E77")
        texto_status.set_text(f"Fase 2: Reconstrução | Inserindo o valor: {val}")

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=counting_sort(meu_array.copy()),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
