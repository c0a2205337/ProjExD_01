import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton = pg.image.load("ex01/fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton_3 = pg.transform.rotozoom(koukaton, 5, 1.0)
    koukaton_5 = pg.transform.rotozoom(koukaton, 5, 1.0)
    koukaton_10 = pg.transform.rotozoom(koukaton, 10, 1.0)
    koukaton_20 = pg.transform.rotozoom(koukaton, 20, 1.0)
    
    kk_list = [koukaton, koukaton_3, koukaton_5, koukaton_10, koukaton_20, koukaton_20, koukaton_10, koukaton_5, koukaton_3, koukaton]
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
            

        screen.blit(kk_list[tmr%9], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()