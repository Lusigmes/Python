import matplotlib.pyplot as plt
import os


plt.rcParams['text.usetex'] = True


os.makedirs("formulas_img", exist_ok=True)

# formulas = [
#     r"\left( \frac{N_{\mathrm{bons}}}{N_{\mathrm{total}}} \right) \times 100\%",
# ]

formulas = [
    r"\mathrm{video\_keypoints} = [\mathrm{frame}][\mathrm{articulacao * coord}]",
]

# formulas = [
#     r"\mathrm{video\_keypoints} = [\mathrm{frame}][\mathrm{articulacao}][\mathrm{coord}]",
#     r"\mathrm{video\_keypoints} = [\mathrm{frame}][\mathrm{pessoa}][\mathrm{articulacao}][\mathrm{coord}]",
# ]

# dtw
# formulas = [
#     r"D(i, j) = d(a_i, b_j) + \min\left\{ \begin{array}{l} D(i-1, j), \\ D(i, j-1), \\ D(i-1, j-1) \end{array} \right\}",

#     r"d(a_i, b_j) = (a_i - b_j)^2",
#     r"d(a_i, b_j) = \sqrt{(a_i - b_j)^2}",
#     r"d(a_i, b_j) = |a_i - b_j|",

#     r"D_{\mathrm{bruta}} = \sum_{(i, j) \in \mathrm{path}} d(a_i, b_j)",
#     r"D_{\mathrm{normalizada}} = \frac{D_{\mathrm{bruta}}}{\mathrm{len(path)}}",
#     r"\mathrm{Erro\_medio} = \frac{1}{N} \sum_{(i, j) \in \mathrm{path}} |a_i - b_j|",
#     r"\mathrm{Desvio} = \sqrt{ \frac{1}{N} \sum_{(i, j) \in \mathrm{path}} \left( |a_i - b_j| - \mathrm{media} \right)^2 }"
# ]

# fft
# formulas = [
#     r"x_n = y_n - \frac{1}{N} \sum_{n=0}^{N-1} y_n",
#     r"X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-i 2 \pi \frac{k n}{N}}",
#     r"|X_k| = \sqrt{\Re(X_k)^2 + \Im(X_k)^2}",
#     r"f_{\mathrm{dom}} = f_k \quad \mathrm{onde} \quad |X_k| = \max(|X|)",
#     r"T = \frac{1}{f_{\mathrm{dom}}}"
# ]

for i, formula in enumerate(formulas, start=1):
    fig, ax = plt.subplots(figsize=(6, 1.5))
    fig.patch.set_alpha(0)  # fundo transparente
    ax.axis('off')

    # Adiciona a fórmula no centro
    ax.text(0.5, 0.5, f"${formula}$", fontsize=20, ha='center', va='center')
    # ax.text(0.5, 0.5, f"${formula}$", fontsize=20, ha='center', va='center', color='white')

    filename = f"formulas_img/formula_{i}.png"
    plt.savefig(filename, dpi=300, transparent=True, bbox_inches='tight')
    plt.close()

print("Imagens geradas com sucesso!")
