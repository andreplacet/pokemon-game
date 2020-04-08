from random import randint, choice
from time import sleep


class Pokemon:
    def __init__(self, apelido=None):
        if apelido:
            self.apelido = apelido
        else:
            self.apelido = self.especie

    def __str__(self):
        return f'{self.especie} LV.{self.level}'

    def atacar(self, inimigo):  # CODIDO DE ATAQUE BASICO
        dano = self.atak - inimigo.defesa
        if dano <= 0:
            dano = 1
        if self.tipo == inimigo.fraqueza:
            if dano <= 0:
                dano = 1
            dano += dano * 1.5
            inimigo.vida -= dano
            if inimigo.vida < 0:
                inimigo.vida = 0
            print(
                f'{self.especie} atacou {inimigo.especie} \n'
                f'E causou CRITICO\n'
                f'\033[33m{dano:.0f}\033[m de dano em {inimigo.especie}\n'
                f'\033[32m{inimigo.vida:.0f}\033[m de vida!')
            sleep(1)
        elif self.tipo == inimigo.vantagem:
            dano -= dano * 1.5
            if dano <= 0:
                dano = 1
            inimigo.vida -= dano
            print(
                f'{self.especie} atacou {inimigo.especie}\n'
                f'E não causou muito dano...\n'
                f'\033[33m{dano:.0f}\033[m de dano em {inimigo.especie}\n'
                f'\033[32m{inimigo.vida:.0f}\033[m de vida!')
            sleep(1)
        else:
            inimigo.vida -= dano
            print(
                f'{self.especie} atacou {inimigo.especie}\n'
                f'E causou \033[33m{dano:.0f}\033[m de dano em{inimigo.especie}\n'
                f'\033[32m{inimigo.vida:.0f}\033[m de vida!')
            sleep(1)

    def ataqueespecial(self, inimigo):  # função responsavel pelos ataques especiais
        dano = self.atakesp - inimigo.defesaesp
        if self.tipo == inimigo.fraqueza:
            dano += dano * 1.5
            if dano <= 0:
                dano = 3
            inimigo.vida -= dano
            if inimigo.vida < 0:
                inimigo.vida = 0
            print(f'{self.especie} usou \033[31m{self.ataquesp}\033[m em {inimigo.especie}\n'
                  f'E causou \033[33m{dano:.0f}\033[m de dano em {inimigo.especie}\n'
                  f'Vida restante: {inimigo.apelido}: \033[32m{inimigo.vida:.0f}\033[m')
            print()
            sleep(1)
        elif self.tipo == inimigo.vantagem:
            dano -= dano * 1.5
            if dano <= 0:
                dano = 3
            inimigo.vida -= dano
            if inimigo.vida < 0:
                inimigo.vida = 0
            print(f'{self.especie} usou \033[31m{self.ataquesp}\033[m em {inimigo.especie}\n'
                  f'E causou \033[33m{dano:.0f}\033[m de dano em {inimigo.especie}\n'
                  f'Vida restante: {inimigo.apelido}: \033[32m{inimigo.vida:.0f}\033[m')
            print()
            sleep(1)
        else:
            if dano <= 0:
                dano = 3
            inimigo.vida -= dano
            if inimigo.vida < 0:
                inimigo.vida = 0
            print(f'{self.especie} usou \033[31m{self.ataquesp}\033[m em {inimigo.especie}\n'
                  f'E causou \033[33m{dano:.0f}\033[m de dano em {inimigo.especie}\n'
                  f'Vida restante: {inimigo.apelido}: \033[32m{inimigo.vida:.0f}\033[m')
            print()
            sleep(1)


class Charmander(Pokemon):
    sex = ['Macho', 'Femêa']
    especie = '\033[31mCharmander\033[m'
    tipo = 'Fogo'
    peso = randint(6, 15)
    altura = randint(1, 3)
    fraqueza = 'Água'
    vantagem = 'Planta'
    sexo = choice(sex)
    ataquesp = 'Bola de Fogo'
    ataquesp2 = 'Arranhão'
    exp = 0

    def __init__(self):
        super().__init__(apelido=None)
        self.level = randint(5, 9)
        if self.level == 5:
            self.atak = randint(5, 10)
            self.defesa = randint(3, 8)
            self.atakesp = randint(8, 14)
            self.defesaesp = randint(6, 10)
            self.speed = randint(2, 4)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        elif 5 < self.level > 8:
            self.atak = randint(7, 12)
            self.defesa = randint(5, 10)
            self.atakesp = randint(12, 18)
            self.defesaesp = randint(10, 16)
            self.speed = randint(4, 6)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        else:
            self.atak = randint(8, 14)
            self.defesa = randint(6, 11)
            self.atakesp = randint(18, 24)
            self.defesaesp = randint(16, 21)
            self.speed = randint(5, 7)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2

    def evolucao(self):
        if self.level >= 16:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[31mCharmeleon\033[m'
            self.tipo = 'Fogo'
            self.peso = randint(12, 28)
            self.altura = randint(1, 2)
            self.vida += 150
            self.maxvida = self.vida
            self.ataquesp = 'Lança Chamas'
            self.ataquesp2 = 'Torre de Chamas'
            self.exp = self.exp
            print()
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
        elif self.level >= 36:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.sex = ['Macho', 'Femêa']
            self.especie = '\033[31mCharizard\033[m'
            self.tipo = 'Fogo'
            self.peso = randint(28, 40)
            self.altura = randint(2, 3)
            self.vida += 300
            self.maxvida = self.vida
            self.ataquesp = 'Lança Chamas'
            self.ataquesp2 = 'Explosão de Fogo'
            self.exp += self.exp
            print()
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)


class Squirtle(Pokemon):
    sex = ['Macho', 'Femêa']
    especie = '\033[34mSquirtle\033[m'
    tipo = 'Água'
    peso = randint(4, 10)
    altura = randint(0, 1)
    fraqueza = 'Planta'
    vantagem = 'Fogo'
    sexo = choice(sex)
    ataquesp = 'Bolhas de Água'
    ataquesp2 = 'Cabeçada'
    exp = 0

    def __init__(self):
        super().__init__()
        self.level = randint(5, 9)
        if self.level == 5:
            self.atak = randint(5, 10)
            self.defesa = randint(3, 8)
            self.atakesp = randint(8, 14)
            self.defesaesp = randint(6, 10)
            self.speed = randint(2, 4)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        elif 5 < self.level > 8:
            self.atak = randint(7, 12)
            self.defesa = randint(5, 10)
            self.atakesp = randint(12, 18)
            self.defesaesp = randint(10, 16)
            self.speed = randint(4, 6)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        else:
            self.atak = randint(8, 14)
            self.defesa = randint(6, 11)
            self.atakesp = randint(18, 24)
            self.defesaesp = randint(16, 21)
            self.speed = randint(5, 7)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2

    def evolucao(self):
        if self.level >= 14:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[34mWartortle\033[m'
            self.tipo = 'Água'
            self.peso = randint(20, 40)
            self.altura += 1
            self.vida += 100
            self.maxvida = self.vida
            self.ataquesp = 'Jato D`água'
            self.ataquesp2 = 'Surf'
            self.exp += self.exp
            print()
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
        elif self.level >= 34:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[34mBlastoise\033[m'
            self.tipo = 'Água'
            self.peso = randint(100, 150)
            self.altura += 1
            self.vida += 250
            self.maxvida = self.vida
            self.ataquesp = 'Surf'
            self.ataquesp2 = 'Hidro Bomba'
            self.exp += self.exp
            print()
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)


class Bulbassaur(Pokemon):
    sex = ['Macho', 'Femêa']
    especie = '\033[32mBulbassaur\033[m'
    tipo = 'Planta'
    peso = randint(1, 7)
    altura = randint(0, 1)
    fraqueza = 'Fogo'
    vantagem = 'Água'
    sexo = choice(sex)
    ataquesp = 'Sementes'
    ataquesp2 = 'Folha Navalha'
    exp = 0

    def __init__(self):
        super().__init__()
        self.level = randint(5, 9)
        if self.level == 5:
            self.atak = randint(5, 10)
            self.defesa = randint(3, 8)
            self.atakesp = randint(8, 14)
            self.defesaesp = randint(6, 10)
            self.speed = randint(2, 4)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        elif 5 < self.level > 8:
            self.atak = randint(7, 12)
            self.defesa = randint(5, 10)
            self.atakesp = randint(12, 18)
            self.defesaesp = randint(10, 16)
            self.speed = randint(4, 6)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        else:
            self.atak = randint(8, 14)
            self.defesa = randint(6, 11)
            self.atakesp = randint(18, 24)
            self.defesaesp = randint(16, 21)
            self.speed = randint(5, 7)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2

    def evolucao(self):
        if self.level >= 14:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[32mIvysaur\033[m'
            self.tipo = 'Planta'
            self.peso = randint(10, 28)
            self.altura += 1
            self.vida += 100
            self.maxvida = self.vida
            self.ataquesp = 'Ataque de Chicote'
            self.ataquesp2 = 'Bomba de Laminas'
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
        elif self.level >= 34:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[32mVenaussaur\033[m'
            self.tipo = 'Planta'
            self.peso = randint(80, 100)
            self.altura += 1
            self.vida += 250
            self.maxvida = self.vida
            self.ataquesp = 'Surf'
            self.ataquesp2 = 'Hidro Bomba'
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)


class Caterpie(Pokemon):
    sex = ['Macho', 'Femêa']
    especie = '\033[32mCaterpie\033[m'
    tipo = 'Inseto'
    peso = randint(1, 7)
    altura = randint(0, 1)
    fraqueza = 'Fogo'
    vantagem = 'Pedra'
    sexo = choice(sex)
    ataquesp = 'Mordida'
    ataquesp2 = 'String Shot'
    exp = 0

    def __init__(self):
        super().__init__()
        self.level = randint(5, 9)
        if self.level == 5:
            self.atak = randint(5, 10)
            self.defesa = randint(3, 8)
            self.atakesp = randint(8, 14)
            self.defesaesp = randint(6, 10)
            self.speed = randint(2, 4)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        elif 5 < self.level > 8:
            self.atak = randint(7, 12)
            self.defesa = randint(5, 10)
            self.atakesp = randint(12, 18)
            self.defesaesp = randint(10, 16)
            self.speed = randint(4, 6)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        else:
            self.atak = randint(8, 14)
            self.defesa = randint(6, 11)
            self.atakesp = randint(18, 24)
            self.defesaesp = randint(16, 21)
            self.speed = randint(5, 7)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2

    def evolucao(self):
        if self.level >= 10:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[32mMetapod\033[m'
            self.tipo = 'Inseto'
            self.peso = randint(10, 28)
            self.altura += 1
            self.vida += 100
            self.maxvida = self.vida
            self.ataquesp = 'Endurecer'
            self.ataquesp2 = 'Bomba de Laminas'
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
        elif self.level >= 12:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[32mButterfree\033[m'
            self.tipo = 'Inseto'
            self.peso = randint(80, 100)
            self.altura += 1
            self.vida += 250
            self.atakesp += (self.level * 1.5)
            self.maxvida = self.vida
            self.ataquesp = 'Whirlwind'
            self.ataquesp2 = 'Raio Psíquico'
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)


class Weedle(Pokemon):
    sex = ['Macho', 'Femêa']
    especie = '\033[33mWeedle\033[m'
    tipo = 'Inseto'
    peso = randint(1, 7)
    altura = randint(0, 1)
    fraqueza = 'Fogo'
    vantagem = 'Pedra'
    sexo = choice(sex)
    ataquesp = 'Espinho venenoso'
    ataquesp2 = 'String Shot'
    exp = 0

    def __init__(self):
        super().__init__()
        self.level = randint(5, 9)
        if self.level == 5:
            self.atak = randint(5, 10)
            self.defesa = randint(3, 8)
            self.atakesp = randint(8, 14)
            self.defesaesp = randint(6, 10)
            self.speed = randint(2, 4)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        elif 5 < self.level > 8:
            self.atak = randint(7, 12)
            self.defesa = randint(5, 10)
            self.atakesp = randint(12, 18)
            self.defesaesp = randint(10, 16)
            self.speed = randint(4, 6)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2
        else:
            self.atak = randint(8, 14)
            self.defesa = randint(6, 11)
            self.atakesp = randint(18, 24)
            self.defesaesp = randint(16, 21)
            self.speed = randint(5, 7)
            self.vida = self.level * 10
            self.maxvida = self.vida
            self.exptoup = self.level * 2

    def evolucao(self):
        if self.level >= 10:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[33mKakuna\033[m'
            self.tipo = 'Inseto'
            self.peso = randint(10, 28)
            self.altura += 1
            self.vida += 100
            self.maxvida = self.vida
            self.ataquesp = 'Endurecer'
            self.ataquesp2 = ''
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
        elif self.level >= 12:
            print(f'O que?? seu Pokemon {self.especie} está '
                  f'evoluindo', end=' ')
            for c in range(3):
                print('.', end='')
                sleep(1)
            self.especie = '\033[33mBeedrill\033[m'
            self.tipo = 'Inseto'
            self.peso = randint(80, 100)
            self.altura += 1
            self.vida += 250
            self.atak += (self.level * 1.5)
            self.maxvida = self.vida
            self.ataquesp = 'Investida'
            self.ataquesp2 = 'Ataque de Chifres'
            self.exp += self.exp
            print(f'Parabens, seu Pokemon evouliu para um {self.especie}')
            sleep(1.5)
