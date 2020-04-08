from time import sleep
from character_scripts import characters
from pokemons_scripts import poke_list
import os


class Pallet:

    def __init__(self):
        self.nome = 'Pallet'
        self.pokemons = poke_list.poke_pallet

    def city_name(self):
        print(f'-=' * 40)
        print(f'{"P A L L E T":^80}')
        print(f'=-' * 40)

    def city(self, player):
        os.system('clear')
        if self.nome not in player.cidades_visitadas:
            player.cidades_visitadas.append(self.nome)
        characters.TelaInicial()
        self.city_name()
        while True:
            print('O que deseja fazer?\n')
            print(f'1 - {"Treinar Pokemons"}       2 - {"Lutar contra Treinadores"}\n'
                                f'3 - {"Ir ao Ginásio"}          4 - {"Trocar de Cidade"}')
            escolha = (input('\n--> '))
            if escolha.isnumeric():
                if int(escolha) == 1:
                    player.batalha_pokemon(pokemon=self.pokemons)
                elif int(escolha) == 2:
                    player.batalha(characters.Rival(pokemons=self.pokemons))
                elif int(escolha) == 3:
                    break
            else:
                print('Caracteres invalido, use os numeros indicados no menu')
                sleep(4)
