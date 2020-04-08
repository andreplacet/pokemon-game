from battle_scripts import batalha
from character_scripts import characters
from time import sleep
from pokemons_scripts import poke_list

import os


if __name__ == '__main__':
    os.system('clear')
    characters.TelaInicial()

    print('\n')
    print(f'Olá Jogador, bem vindo ao jogo Pokemon RPG de terminal', end=' ')
    for _ in range(3):
        print('.', end='')
        sleep(0.5)
    print('\n')
    sleep(0.5)
    nome = str(input('Qual o seu nome aventureiro? --> ')).capitalize()
    jogador = characters.Player(nome=nome)
    print()
    print('Hmmm... ')
    sleep(1.5)
    print(f'muito bem, muito prazer \033[31m{nome}\033[m, Vamos começar nossa aventura!!')
    print()
    sleep(2.5)
    dialogo_inicial = ['\033[33mVocê acaba de entrar em um mundo repleto de monstros com poderes fantásticos!!',
                       'E o que fazemos com eles???', 'Tiramos eles de seu habitat natural de paz e alegria',
                       'E colocamos eles pra fazer rinha nessa porra!!!\033[m']
    for _ in dialogo_inicial:
        print(_)
        sleep(2)
    print()
    sleep(0.5)
    dialogo_poke_inicial = ['\033[33mPara encarar sua aventura você vai precisar de um Pokemon',
                            'Como eu estou de bom humor e fui com a sua cara',
                            'Eu vou te arrumar um Pokemon para sua jornada!!!\033[m']
    for _ in dialogo_poke_inicial:
        print(_)
        sleep(2)
    print('\n')
    print(f'Escolha entre esses pokemons para iniciar sua jornada:')
    print()
    for _ in range(len(poke_list.pokemons_iniciais)):
        print(f'    {_ + 1}:{poke_list.pokemons_iniciais[_]}', end=' ')
    print('\n')
    escolha = int(input('--> '))
    print(f'\nParabéns, voce escolheu {poke_list.pokemons_iniciais[(escolha - 1)].apelido}\n')
    sleep(2)
    jogador.pokemons.append(characters.poke_list.pokemons_iniciais[(escolha - 1)])
    poke_list.pokemons_iniciais.remove(poke_list.pokemons_iniciais[(escolha - 1)])
    rival = characters.Rival(nome='Gary')
    dialogo_treta = [f'\033[33mVamos testar sua habilidade, esse é meu neto, {rival.nome}!!!',
                     'Ele também esta iniciando sua jornada hoje',
                     'Acredito que uma Batalha pode ser interessante...', 'Vamos lá!!!\033[m']
    for _ in dialogo_treta:
        print(_)
    print('\nPrepare-se !!!')
    sleep(1)
    jogador.batalha(rival)
    print()
    dialogo_postreta = ['\033[33mEnfim...', 'Agora vocẽs entendem como funcionam as batalhas pokemons',
                        'vão explocar e escravizar mais alguns desses monstrinhos!!!\033m']
    for _ in dialogo_postreta:
        print(_)
        sleep(3)
    print('\n')
    os.system('clear')
    characters.TelaInicial()
    ().city(player=jogador)
