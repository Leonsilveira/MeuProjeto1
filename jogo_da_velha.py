import tkinter as tk
from tkinter import messagebox

class JogoDaVelhaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")

        self.jogador_atual = "X"
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

        # Adicionar as linhas abaixo para a contagem de pontos
        self.pontos_x = 0
        self.pontos_o = 0

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(master, text=" ", font=("Helvetica", 24), width=4, height=2,
                                              command=lambda row=i, col=j: self.realizar_jogada(row, col))
                self.botoes[i][j].grid(row=i, column=j)

    def realizar_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual, state="disabled")

            if self.verificar_vitoria():
                messagebox.showinfo("Vitória!", f"Jogador {self.jogador_atual} venceu!")
                self.exibir_pontuacao()
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Empate!", "O jogo terminou em empate.")
                self.exibir_pontuacao()
                self.resetar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        # ... (seu código existente)

        # Verificar vencedor
        for i in range(3):
            if all(self.tabuleiro[i][j] == self.jogador_atual for j in range(3)) or \
               all(self.tabuleiro[j][i] == self.jogador_atual for j in range(3)):
                # Jogador venceu, atualizar pontos
                if self.jogador_atual == "X":
                    self.pontos_x += 1
                else:
                    self.pontos_o += 1
                return True

        # Verificar diagonais
        if all(self.tabuleiro[i][i] == self.jogador_atual for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == self.jogador_atual for i in range(3)):
            # Jogador venceu, atualizar pontos
            if self.jogador_atual == "X":
                self.pontos_x += 1
            else:
                self.pontos_o += 1
            return True

        return False

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))

    def resetar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=" ", state="active")
                self.tabuleiro[i][j] = " "
        self.jogador_atual = "X"

    def exibir_pontuacao(self):
        mensagem = f"Pontuação:\nJogador X: {self.pontos_x}\nJogador O: {self.pontos_o}"
        messagebox.showinfo("Pontuação", mensagem)


if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_velha_gui = JogoDaVelhaGUI(root)
    root.mainloop()