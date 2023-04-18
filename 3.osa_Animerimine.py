from lib2to3 import pygram
import pygame,sys

pygame.init()
#värvid
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animatsion")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("bee.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False
samm=2
while not lõpp:
	kell.tick(60)
	events=pygame.event.get()
	for i in pygame.event.get():
		if i.type==pygame.QUIT():
			sys.exit()
	ekraan.blit(mesilane,(posX,posY))
	posX-=samm
	if posX>X-mesilane.get_rect().width or posX<0:
		samm=-samm

	pygame.display.flip()
	ekraan.fill(roheline)
pygame.quit()