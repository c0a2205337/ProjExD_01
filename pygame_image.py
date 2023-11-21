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
    koukaton_10 = pg.transform.rotozoom(koukaton, 5, 1.0)
    koukaton_20 = pg.transform.rotozoom(koukaton, 10, 1.0)
    kk_list = [koukaton, koukaton_10, koukaton_20, koukaton_10]
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(kk_list[tmr%4], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()