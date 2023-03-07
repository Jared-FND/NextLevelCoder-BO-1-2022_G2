from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()
    death_count = 0
    while game.game_running:
        if not game.playing:
            game.show_menu(death_count=death_count)
            death_count += 1


# TAREA CLASE 4:
# HACER UN MENU MAS BONITO :) , puede ser mas colores, mas imagenes, otras fuentes 
# PONERLE MUSIQUITA AL JUEGO
