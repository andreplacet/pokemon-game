from random import randint, choice
from characters import TelaInicial, Rival
from poke_list import *
import os


class Pallet:

    def __init__(self):
        self.nome = 'Pallet'
        self.pokemons = poke_pallet
        self.ginasio = []

    def city_name(self):
        print(f'-=' * 40)
        print(f'{"P A L L E T":^80}')
        print(f'=-' * 40)

    def city(self, player):
        os.system('clear')
        if self.nome not in player.cidades_visitadas:
            player.cidades_visitadas.append(self.nome)
        TelaInicial()
        self.city_name()
        while True:
            print('O que deseja fazer?\n')
            print(f'1 - {"Treinar Pokemons"}       2 - {"Lutar contra Treinadores"}\n'
                                f'3 - {"Ir ao Ginásio"}          4 - {"Trocar de Cidade"}')
            escolha = int(input('\n--> '))
            if escolha == 1:
                player.batalha_pokemon(pokemon=poke_pallet)
            elif escolha == 2:
                player.batalha(Rival(pokemons=poke_pallet))
            elif escolha == 3:
                break