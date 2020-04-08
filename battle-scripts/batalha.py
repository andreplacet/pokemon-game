'''def batalhar(self, enemy):
    print(f'{self} iniciou uma batalha contra {enemy}!')
    enemy.show_pokemons()
    pokemon_inimigo = enemy.escolher_pokemon()
    pokemon_player = self.escolher_pokemon()
    if pokemon_player and pokemon_inimigo:
        while True:
            vitoria = pokemon_player.atacar(inimigo=pokemon_inimigo)
            if vitoria:
                print(f'{self} Ganhou a batalha!')
                print(f'{pokemon_player} ganhou {pokemon_inimigo.level * 1.5:.0f} pontos de Exp')
                pokemon_player.exp += int(f'{pokemon_inimigo.level * 1.5:.0f}')
                if pokemon_player.exp == pokemon_player.exptoup:
                    pokemon_player.level += 1
                    pokemon_player.atak += randint(1, 4)
                    pokemon_player.defesa += randint(1, 4)
                    pokemon_player.atakesp += randint(2, 4)
                    pokemon_player.defesaesp += randint(2, 4)
                    pokemon_player.speed += randint(1, 4)
                    pokemon_player.exptoup = int(pokemon_player.exptoup * 2)
                    pokemon_player.evolucao()
                break
            self.money += randint(20, 30)
            vitoria_inimiga = pokemon_inimigo.atacar(inimigo=pokemon_player)
            if vitoria_inimiga:
                print(f'{enemy} Ganhou a bataha!')
                print(f'{pokemon_player.apelido} ganhou {pokemon_inimigo.level * 1.2:.0f} pontos de Exp')
                pokemon_player.exp += int(f'{pokemon_inimigo.level * 1.2:.0f}')
                if pokemon_player.exp == pokemon_player.exptoup:
                    pokemon_player.level += 1
                    pokemon_player.atak += randint(1, 4)
                    pokemon_player.defesa += randint(1, 4)
                    pokemon_player.atakesp += randint(2, 4)
                    pokemon_player.defesaesp += randint(2, 4)
                    pokemon_player.speed += randint(1, 4)
                    pokemon_player.exptoup = int(pokemon_player.exptoup * 2)
                    pokemon_player.evolucao()
                break
            self.money += randint(20, 30)
    else:
        print('Os personagens não possuem Pokemons!!')'''