import pygame
import os
from pygame.locals import *
from tkinter import simpledialog, Tk

pygame.init()
relogio = pygame.time.Clock()
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Maker")
branco = (255, 255, 255)
preto = (0, 0, 0)
fundo = pygame.image.load("Assets/bg.jpg")
tela.blit(fundo, (0, 0))
pygame.display.set_caption("Gerenciador de Marcações")

def salvar_marcacoes(marcacoes, arquivo="marcacoes.txt"):
    with open(arquivo, 'w') as f:
        for nome, posicao in marcacoes.items():
            f.write(f"{nome} {posicao[0]} {posicao[1]}\n")

def carregar_marcacoes(arquivo="marcacoes.txt"):
    marcacoes = {}
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r') as f:
                for linha in f:
                    nome, x, y = linha.strip().split()
                    marcacoes[nome] = (int(x), int(y))
        except Exception as e:
            print(f"Erro ao carregar marcações: {e}")
    else:
        open(arquivo, 'w').close()  
    return marcacoes

def excluir_marcacoes(arquivo="marcacoes.txt"):
    if os.path.exists(arquivo):
        os.remove(arquivo)
    return {}

def main():
    global estrelas
    marcacoes = carregar_marcacoes()
    marcacoes_ordem = list(marcacoes.values())
    
    root = Tk()
    root.withdraw()  

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salvar_marcacoes(marcacoes)
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    salvar_marcacoes(marcacoes)
                    pygame.quit()
                    quit()
                elif evento.key == pygame.K_F10:
                    salvar_marcacoes(marcacoes)
                elif evento.key == pygame.K_F11:
                    marcacoes = carregar_marcacoes()
                    marcacoes_ordem = list(marcacoes.values())
                elif evento.key == pygame.K_F12:
                    marcacoes = excluir_marcacoes()
                    marcacoes_ordem = list(marcacoes.values())
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    posicao = pygame.mouse.get_pos()
                    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
                    if not nome:
                        nome = f"desconhecido_{posicao}"
                    marcacoes[nome] = posicao
                    marcacoes_ordem.append(posicao)

        tela.blit(fundo, (0, 0))

        if len(marcacoes_ordem) > 1:
            pygame.draw.lines(tela, branco, False, marcacoes_ordem, 1)

        for nome, posicao in marcacoes.items():
            pygame.draw.circle(tela, branco, posicao, 5)
            texto = pygame.font.SysFont("Arial", 20).render(nome, True, branco)
            tela.blit(texto, (posicao[0] + 10, posicao[1]))

        fonte = pygame.font.SysFont("Arial", 30)
        salvarTexto = fonte.render("Pressione F10 para salvar", True, branco)
        carregarTexto = fonte.render("Pressione F11 para carregar", True, branco)
        excluirTexto = fonte.render("Pressione F12 para excluir todas as marcações", True, branco)
        tela.blit(salvarTexto, (10, 10))
        tela.blit(carregarTexto, (10, 40))
        tela.blit(excluirTexto, (10, 70))

        pygame.display.flip()
        relogio.tick(60)

if __name__ == "__main__":
    main()