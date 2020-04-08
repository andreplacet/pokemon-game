from random import randint, choice
from poke_list import POKEMONS
from time import sleep
import os

NOMES = ['Valberto', 'Joelson', 'Cláudio', 'Ronaldo', 'Emanuel', 'Cleison', 'Ricardo']


def TelaInicial():
    print('\033[31;47m=-' * 40)
    print(f'{"POKEMON RPG DE TERMINAL":^80}')
    print('-=' * 40)
    print('\033[m')


# INSTANCIA DE PERSONAGEM GERAL
class MainCharacter:

    def __init__(self, nome=None, pokemons=[], itens=[], box=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = 'Cidadão'
        self.pokemons = pokemons
        self.itens = itens
        self.box = box
        self.money = 0

    def __str__(self):
        return self.nome

    def show_pokemons(self):
        if self.pokemons:
            print(f'\nPokemons de {self.nome}:')
            for c in range(len(self.pokemons)):
                print(f'{c + 1}: \033[31m|\033[m{self.pokemons[c]}\033[31m|\033[m', end=' ')
            print()
        else:
            print(f'{self} não possui Pokemons!')

    def show_itens(self):
        for item in self.itens:
            print(f'Lista de Itens:\n{item}')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhio = choice(self.pokemons)
            p = f'\n{self} escolheu {pokemon_escolhio}'
            for letra in p:
                print(letra, end='')
            print()
            return pokemon_escolhio
        else:
            print(f'{self} Não possui Pokemons!!!')

    def batalha(self, enemy):
        meu_pokemon = self.escolher_pokemon()
        enemy_pokemon = enemy.escolher_pokemon()
        enemy.show_pokemons()
        os.system('clear')
        TelaInicial()
        print(f'{self} iniciou uma batalha conta {enemy.nome}!!')
        if meu_pokemon and enemy_pokemon:
            while True:
                print()
                print(f'{meu_pokemon.apelido}: \033[32mHP({meu_pokemon.vida:.0f})\033[m         '
                      f'{enemy_pokemon.apelido}: \033[32m'
                      f' HP({enemy_pokemon.vida:.0f})\033[m')
                print()
                print(f'Escolha seu ataque')
                escolha = int(input(f'  1  -> Ataque normal\n'
                                    f'  2 -> {meu_pokemon.ataquesp}\n'
                                    f' --> '))
                if escolha == 1:
                    meu_pokemon.atacar(enemy_pokemon)
                    enemy_pokemon.atacar(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                elif escolha == 2:
                    meu_pokemon.ataqueespecial(enemy_pokemon)
                    enemy_pokemon.ataqueespecial(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                elif escolha == 3:
                    meu_pokemon.ataqueespecial(enemy_pokemon)
                    meu_pokemon.ataqueespecial(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                else:
                    meu_pokemon.ataqueespecial(enemy_pokemon)
                    meu_pokemon.ataqueespecial(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                if meu_pokemon.vida <= 0:
                    print(f'{enemy} Ganhou a bataha!')
                    print(f'{meu_pokemon.apelido} ganhou {enemy_pokemon.level * 1.2:.0f} pontos de Exp')
                    meu_pokemon.exp += int(f'{enemy_pokemon.level * 1.2:.0f}')
                    sleep(4)
                    os.system('clear')
                    TelaInicial()
                    meu_pokemon.vida = meu_pokemon.maxvida
                    if meu_pokemon.exp == meu_pokemon.exptoup:
                        print(f'{meu_pokemon.apelido} subiu de level!')
                        meu_pokemon.level += 1
                        meu_pokemon.atak += randint(1, 4)
                        meu_pokemon.defesa += randint(1, 4)
                        meu_pokemon.atakesp += randint(2, 4)
                        meu_pokemon.defesaesp += randint(2, 4)
                        meu_pokemon.speed += randint(1, 4)
                        meu_pokemon.maxvida += int(meu_pokemon.level * 1.5)
                        meu_pokemon.exptoup = int(meu_pokemon.exptoup * 2)
                        meu_pokemon.evolucao()
                    break
                elif enemy_pokemon.vida <= 0:
                    print(f'{self} Ganhou a bataha!')
                    print(f'{meu_pokemon.apelido} ganhou {enemy_pokemon.level * 1.2:.0f} pontos de Exp')
                    meu_pokemon.exp += int(f'{enemy_pokemon.level * 1.2:.0f}')
                    sleep(4)
                    os.system('clear')
                    TelaInicial()
                    meu_pokemon.vida = meu_pokemon.maxvida
                    if meu_pokemon.exp == meu_pokemon.exptoup:
                        print(f'{meu_pokemon.apelido} subiu de level!')
                        meu_pokemon.level += 1
                        meu_pokemon.atak += randint(1, 4)
                        meu_pokemon.defesa += randint(1, 4)
                        meu_pokemon.atakesp += randint(2, 4)
                        meu_pokemon.defesaesp += randint(2, 4)
                        meu_pokemon.speed += randint(1, 4)
                        meu_pokemon.maxvida += int(meu_pokemon.level * 1.5)
                        meu_pokemon.exptoup = int(meu_pokemon.exptoup * 2)
                        meu_pokemon.evolucao()
                    break
        else:
            print('Os jogadores não possuem pokemons')

    def batalha_pokemon(self, pokemon):
        meu_pokemon = self.escolher_pokemon()
        enemy_pokemon = choice(pokemon)
        os.system('clear')
        TelaInicial()
        print(f'{self} começou uma batalha contra o pokemon selvagem {enemy_pokemon.especie}')
        if meu_pokemon and enemy_pokemon:
            while True:
                print()
                print(f'{meu_pokemon.apelido}: \033[32mHP({meu_pokemon.vida:.0f})\033[m         '
                      f'{enemy_pokemon.apelido}: \033[32m'
                      f' HP({enemy_pokemon.vida:.0f})\033[m')
                print()
                print(f'Escolha seu ataque')
                escolha = int(input(f'  1  -> Ataque normal\n'
                                    f'  2 -> {meu_pokemon.ataquesp}\n'
                                    f' --> '))
                if escolha == 1:
                    meu_pokemon.atacar(enemy_pokemon)
                    enemy_pokemon.atacar(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                elif escolha == 2:
                    meu_pokemon.ataqueespecial(enemy_pokemon)
                    enemy_pokemon.ataqueespecial(meu_pokemon)
                    os.system('clear')
                    TelaInicial()

                else:
                    meu_pokemon.ataqueespecial(enemy_pokemon)
                    meu_pokemon.ataqueespecial(meu_pokemon)
                    os.system('clear')
                    TelaInicial()
                if meu_pokemon.vida <= 0:
                    print(f'{enemy_pokemon.especie} Ganhou a bataha!')
                    print(f'{meu_pokemon.apelido} ganhou {enemy_pokemon.level * 1.2:.0f} pontos de Exp')
                    meu_pokemon.exp += int(f'{enemy_pokemon.level * 1.2:.0f}')
                    sleep(4)
                    os.system('clear')
                    TelaInicial()
                    meu_pokemon.vida = meu_pokemon.maxvida
                    if meu_pokemon.exp == meu_pokemon.exptoup:
                        print(f'{meu_pokemon.apelido} subiu de level!')
                        meu_pokemon.level += 1
                        meu_pokemon.atak += randint(1, 4)
                        meu_pokemon.defesa += randint(1, 4)
                        meu_pokemon.atakesp += randint(2, 4)
                        meu_pokemon.defesaesp += randint(2, 4)
                        meu_pokemon.speed += randint(1, 4)
                        meu_pokemon.maxvida += int(meu_pokemon.level * 1.5)
                        meu_pokemon.exptoup = int(meu_pokemon.exptoup * 2)
                        meu_pokemon.evolucao()
                    break
                elif enemy_pokemon.vida <= 0:
                    print(f'{self} Ganhou a bataha!')
                    print(f'{meu_pokemon.apelido} ganhou {enemy_pokemon.level * 1.5:.0f} pontos de Exp')
                    meu_pokemon.exp += int(f'{enemy_pokemon.level * 1.5:.0f}')
                    sleep(4)
                    os.system('clear')
                    TelaInicial()
                    meu_pokemon.vida = meu_pokemon.maxvida
                    if meu_pokemon.exp == meu_pokemon.exptoup:
                        print(f'{meu_pokemon.apelido} subiu de level!')
                        meu_pokemon.level += 1
                        meu_pokemon.atak += randint(1, 4)
                        meu_pokemon.defesa += randint(1, 4)
                        meu_pokemon.atakesp += randint(2, 4)
                        meu_pokemon.defesaesp += randint(2, 4)
                        meu_pokemon.speed += randint(1, 4)
                        meu_pokemon.maxvida += int(meu_pokemon.level * 1.5)
                        meu_pokemon.exptoup = int(meu_pokemon.exptoup * 2)
                        meu_pokemon.evolucao()
                    break
        else:
            print('Os jogadores não possuem pokemons')


# Criação da Classe Filho - PLAYER(JOGADOR)
class Player(MainCharacter):
    tipo = 'Player'
    cidades_visitadas = []
    cidade_atual = ''
    gym_badges = []

    def caputar(self, pokemon):
        if len(self.pokemons) >= 6:
            self.box.append(pokemon)
            print(f'O pokemons: {pokemon} foi capturado e\n'
                  f'mandando para o BOX')
        else:
            self.pokemons.append(pokemon)
            print(f'{self} capturou um {pokemon}!!')

    def buy_itens(self, item):
        self.itens.append(item)
        print(f'Você adquiriu um {item}!!!')

    def use_itens(self, item, pokemon):
        self.pokemons[pokemon] = self.itens[item]

    def escolher_pokemon(self):
        self.show_pokemons()
        if self.pokemons:
            while True:
                escolha = int(input('\nEscolha seu pokemon: '))
                try:
                    pokemon_escolido = escolha
                    poke_choice = self.pokemons[pokemon_escolido - 1]
                    print(f'\n\033[31m{poke_choice}\033[m eu escolho você!!!')
                    return poke_choice
                except:
                    print('Escolha Invalida!!')
        else:
            print(f'{self} Não possui Pokemons!!!')


# Criação Rival - INIMIGO/ENEMY
class Rival(MainCharacter):
    tipo = 'Rival'

    def __init__(self, nome=None, pokemons=[]):
        super().__init__(nome, pokemons)
        if not nome:
            self.nome = choice(NOMES)
        if not pokemons:
            for i in range(randint(1, 3)):
                pokemons.append(choice(POKEMONS))
