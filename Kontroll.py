import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("volskaja")

ekraani_pind.fill((0,0,0))
pygame.draw.circle(ekraani_pind, (255, 255, 255), (160, 120), 50) # Рисует тело снеговика
pygame.draw.circle(ekraani_pind, (255, 255, 255), (160, 70), 35)
pygame.draw.circle(ekraani_pind, (255, 255, 255), (160, 40), 25)

pygame.draw.circle(ekraani_pind, (0, 0, 0), (150, 35), 5)  # Рисует глаза #левый
pygame.draw.circle(ekraani_pind, (0, 0, 0), (170, 35), 5)  # правый

pygame.draw.polygon(ekraani_pind, (255, 100, 0), [(160, 65), (155, 45), (165, 45)])  #рисует нос

pygame.draw.line(ekraani_pind, (120,69,19), (125, 70), (120, 100), 5)#Добавляем руки #левая рука
pygame.draw.line(ekraani_pind, (120,69,19), (193, 70), (200, 100), 5) # равая рука

pygame.draw.rect(ekraani_pind, (139,69,19), pygame.Rect(190, 90, 15, 50)) #Добавляем дубинку



pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()