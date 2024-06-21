import pygame

# Initializer o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load('ex21.mp3')

# Tocar o arquivo MP3
pygame.mixer.music.play()

# Manter o programa rodando enquanto o áudio é reproduzido
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
