#LifeCounter
import time  # Importa o módulo time para controlar o tempo de exibição da mensagem

class LifeCounter:
    def __init__(self, initial_lives=3):
        self.max_lives = initial_lives  # Número máximo de vidas permitidas
        self.vidas_restantes = initial_lives  # Vidas restantes do jogador
        self.alive = True
        self.death_message_time = None  # Tempo de início da exibição da mensagem de morte

    def get_vidas_restantes(self):
        return self.vidas_restantes

    def perder_vida(self):
        if self.vidas_restantes > 0:
            self.vidas_restantes -= 1
            if self.vidas_restantes == 0:
                self.alive = False
                self.death_message_time = time.time()  # Registra o tempo de início da exibição da mensagem

    def is_alive(self):
        return self.alive

    def show_death_message(self):
        # Verifica se a mensagem de morte deve ser exibida
        if not self.alive and self.death_message_time is not None:
            current_time = time.time()
            elapsed_time = current_time - self.death_message_time
            if elapsed_time < 2:  # Exibe a mensagem por 2 segundos
                print("Você morreu!")  # Aqui você pode substituir por qualquer função de exibição de mensagem