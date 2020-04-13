import matplotlib.pyplot as plt
import numpy as np


class plot_log_exp:
    def __init__(self, tempo=2, pontos=100):
        self.tempo = tempo
        self.pontos = pontos
        self.tempo_array = np.linspace(0.01, self.tempo, self.pontos)
        self.log_array = np.log10(self.tempo_array) - np.log10(0.01)
        self.exp_array = np.exp(self.tempo_array) - 1

    def plot(self, ax, label_y='y', label_x='Tempo', cor_log='g',
             cor_exp='r', texto_log='log', texto_exp='exp', valores=False):
        # linhas do gráfico
        ax.plot(self.tempo_array, self.log_array, cor_log)
        ax.plot(self.tempo_array, self.exp_array, cor_exp)

        # títulos dos eixos
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
        ax.xaxis.label.set_size(14)
        ax.yaxis.label.set_size(14)

        # texto do gráfico
        # está hardcoded... ainda não achei uma forma de o texto se posicionar
        # automaticamente com base em algum critério matemático. Estes valores
        # funcionam bem se não forem alterados o input default de tempo
        ax.annotate(texto_log, (0.2, 1.9), color=cor_log, fontsize=12)
        ax.annotate(texto_exp, (1.25, 5), color=cor_exp, fontsize=12)

        if not valores:
            # remove ticks e tick labels
            ax.tick_params(axis='both', bottom=False, left=False,
                           labelbottom=False, labelleft=False)
        return ax


if __name__ == "__main__":
    fig, arr = plt.subplots(nrows=1, ncols=2, facecolor=(1, 1, 1),
                            figsize=(12, 4))

    plt.subplots_adjust(top=0.98,
                        bottom=0.125,
                        left=0.05,
                        right=0.98,
                        hspace=0.2,
                        wspace=0.2)

    plot_design = plot_log_exp()
    plot_custo = plot_log_exp()

    plot_design.plot(ax=arr[0], label_y='Funcionalidades\nacumuladas',
                     cor_log='r', cor_exp='g', texto_log='Design ruim',
                     texto_exp='Design bom')
    plot_custo.plot(ax=arr[1], label_y='Custo',
                    cor_log='g', cor_exp='r', texto_log='Design bom',
                    texto_exp='Design ruim')
    # plt.savefig('graficos_design.png')  # caso queira salvar
    plt.show()
