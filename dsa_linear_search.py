import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation

meu_array = [7, 12, 9, 4, 11, 5, 3, 8, 6, 10, 2, 1, 15, 14, 13, 16, 20, 18, 17, 19]
alvo = 14


def linear_search(arr, target):
    for i in range(len(arr)):
        yield arr, i, -1, False
        if arr[i] == target:
            yield arr, i, i, True
            return
    yield arr, -1, -1, True


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
    arr, idx, found_idx, finalizado = frame

    for k, barra in enumerate(barras):
        barra.set_color("#4A90E2")

    if finalizado:
        if found_idx != -1:
            for k, barra in enumerate(barras):
                if k != found_idx:
                    barra.set_color("#B9D3F9")
            barras[found_idx].set_color("#50E3C2")
            texto_status.set_text(
                f"BUSCA CONCLUÍDA! Valor {alvo} encontrado no índice {found_idx}."
            )
        else:
            for barra in barras:
                barra.set_color("#E94E77")
            texto_status.set_text(f"BUSCA CONCLUÍDA! Valor {alvo} não encontrado.")
        return barras

    if idx != -1:
        barras[idx].set_color("#F5A623")
        texto_status.set_text(
            f"Buscando alvo ({alvo}) | Inspecionando índice {idx} (valor: {arr[idx]})"
        )

    return barras


anim = animation.FuncAnimation(
    fig,
    func=atualizar,
    frames=linear_search(meu_array, alvo),
    interval=100,
    repeat=False,
    cache_frame_data=False,
)

plt.tight_layout()
plt.show()
