import pygame

def lill_keskel():
    
    lill=pygame.Rect(180,100,240,200)
    pygame.draw.ellipse(ekraani_pind,(80,0,155),lill)
    x=200
    y=100
    x_w=200
    y_h=180
    for i in range(12):
        #ticks=pygame.time.get_ticks()
        lill_väike=pygame.Rect(x,y,x_w,y_h)
        pygame.draw.ellipse(ekraani_pind,(205,50,255),lill_väike,i+2)
        x+=10
        y+=10
        x_w-=20
        y_h-=15
        #pygame.time.wait(200)
pygame.init()
kollane=[255,255,10]
punane=[255,0,0]
varv=[200,200,200]

ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)
hall=[120,120,120]
pygame.draw.circle(ekraani_pind,hall,(500,100),50)
pygame.draw.circle(ekraani_pind,hall,(550,150),60)
pygame.draw.line(ekraani_pind,(22,105,44),(300,180),(300,400),20)

pilt=pygame.image.load("bee.png")
pilt=pygame.transform.scale(pilt,(70,70))
ekraani_pind.blit(pilt,(300,50))

font=pygame.font.SysFont("Broadway",40)
sõnad="Tere tulemast!"

teksti_lisamine=font.render(sõnad,False,varv)
ekraani_pind.blit(teksti_lisamine,(250,25))

lopp_x=300
lopp_y=0
for i in range(30):
    pygame.draw.line(ekraani_pind,kollane,(0,0),(lopp_x,lopp_y),3)
    lopp_x-=10
    lopp_y+=12
lill_keskel()
pygame.display.flip()
while True:   
    #lill_keskel()
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        
        break
    
pygame.quit()