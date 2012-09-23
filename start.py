#!/usr/bin/env python

"""An zoomed image viewer that demonstrates Surface.scroll

This example shows a scrollable image that has a zoom factor of eight.
It uses the Surface.scroll function to shift the image on the display
surface. A clip rectangle protects a margin area. If called as a function,
the example accepts an optional image file path. If run as a program
it takes an optional file path command line argument. If no file
is provided a default image file is used.

When running click on a black triangle to move one pixel in the direction
the triangle points. Or use the arrow keys. Close the window or press ESC
to quit.

"""

import sys
import os

import pygame
from pygame.transform import scale
from pygame.locals import *

main_dir = os.path.dirname(os.path.abspath(__file__))

DIR_UP = 1
DIR_DOWN = 2
DIR_LEFT = 3
DIR_RIGHT = 4

zoom_factor = 1
move_speed = 10

def draw_arrow(surf, color, posn, direction):
    x, y = posn
    if direction == DIR_UP:
        pointlist = ((x - 29, y + 30), (x + 30, y + 30),
                     (x + 1, y - 29), (x, y - 29))
    elif direction == DIR_DOWN:
        pointlist = ((x - 29, y - 29), (x + 30, y - 29),
                     (x + 1, y + 30), (x, y + 30))
    elif direction == DIR_LEFT:
        pointlist = ((x + 30, y - 29), (x + 30, y + 30),
                     (x - 29, y + 1), (x - 29, y))
    else:
        pointlist = ((x - 29, y - 29), (x - 29, y + 30),
                     (x + 30, y + 1), (x + 30, y))
    pygame.draw.polygon(surf, color, pointlist)

def add_arrow_button(screen, regions, posn, direction):
    draw_arrow(screen, Color('black'), posn, direction)
    draw_arrow(regions, (direction, 0, 0), posn, direction)

def scroll_view(screen, image, direction, view_rect):
    dx = dy = 0
    src_rect = None
    zoom_view_rect = screen.get_clip()
    image_w, image_h = image.get_size()
    if direction == DIR_UP:
        if view_rect.top > 0:
            screen.scroll(dy=zoom_factor*move_speed)
            view_rect.move_ip(0, -move_speed)
            src_rect = view_rect.copy()
            src_rect.h = move_speed
            dst_rect = zoom_view_rect.copy()
            dst_rect.h = zoom_factor*move_speed
    elif direction == DIR_DOWN:
        if view_rect.bottom < image_h-move_speed:
            screen.scroll(dy=-zoom_factor*move_speed)
            view_rect.move_ip(0, move_speed)
            src_rect = view_rect.copy()
            src_rect.h = move_speed
            src_rect.bottom = view_rect.bottom
            dst_rect = zoom_view_rect.copy()
            dst_rect.h = zoom_factor*move_speed
            dst_rect.bottom = zoom_view_rect.bottom
    elif direction == DIR_LEFT:
        if view_rect.left > 0:
            screen.scroll(dx=zoom_factor*move_speed)
            view_rect.move_ip(-move_speed, 0)
            src_rect = view_rect.copy()
            src_rect.w = move_speed
            dst_rect = zoom_view_rect.copy()
            dst_rect.w = zoom_factor*move_speed
    elif direction == DIR_RIGHT:
        if view_rect.right < image_w-move_speed:
            screen.scroll(dx=-zoom_factor*move_speed)
            view_rect.move_ip(move_speed, 0)
            src_rect = view_rect.copy()
            src_rect.w = move_speed
            src_rect.right = view_rect.right
            dst_rect = zoom_view_rect.copy()
            dst_rect.w = zoom_factor*move_speed
            dst_rect.right = zoom_view_rect.right
    if src_rect is not None:
        scale(image.subsurface(src_rect),
              dst_rect.size,
              screen.subsurface(dst_rect))
        pygame.display.update(zoom_view_rect)

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()


def put_army(army_image, position, size, player):
    "puts the army into the position with army size caption"
    global image
    army_w, army_h = army_image.get_size()
    font_size = 30
    yellow = (250, 250, 0)
    red = (250, 120, 120)
    black = (10, 10, 10)
    white = (250, 250, 250)
    orange = (250, 250, 128)
    
    if player == 1:
	color = yellow
    else:
	color = red
    
    if pygame.font:
	font = pygame.font.Font(None, font_size)
    	text = font.render(size + "", 1, color)
    	text_bg = font.render(size + "", 1, black)
    	text_w, text_h = text.get_size()
    	text_x = position[0]+(army_w - text_w)/2
    	text_y = position[1] + army_h + 3
    	image.blit(text_bg, (text_x+1, text_y+1))
    	image.blit(text_bg, (text_x-1, text_y+1))
    	image.blit(text_bg, (text_x-1, text_y-1))
    	image.blit(text_bg, (text_x+1, text_y-1))
    	image.blit(text, (text_x, text_y))
        image.blit(army_image, position)

def conv(num):
    return num/27.3*920

def main(image_file=None):
    if image_file is None:
        image_file = os.path.join(main_dir, 'data', 'map.jpg')

    margin = 20
    # view_size = (1300, 650)
    # view_size = (1100, 850)
    view_size = (1100, 650)
    zoom_view_size = (view_size[0] * zoom_factor,
                      view_size[1] * zoom_factor)
    win_size = (zoom_view_size[0] + 2 * margin,
                zoom_view_size[1] + 2 * margin)
    background_color = Color('beige')

    pygame.init()
    # set up key repeating so we can hold down the key to scroll.
    old_k_delay, old_k_interval = pygame.key.get_repeat ()
    pygame.key.set_repeat (500, 30)

    try:
        screen = pygame.display.set_mode(win_size)
        screen.fill(background_color)
        pygame.display.flip()

	global image

        image = pygame.image.load(image_file).convert()
        image_w, image_h = image.get_size()

	orc = load_image('orc.gif')
	elf = load_image('elf.gif')
	nazgul = load_image('nazgul.gif')
	troll = load_image('troll.gif')
	wolf = load_image('wolf.gif')
	wildman = load_image('wildman.gif') # not used
	cavalry = load_image('cavalry.gif')
	dwarf = load_image('dwarf.gif')
	infantry = load_image('infantry.gif')

	put_army(orc,(920,220),"500",2) # Mount Gundabad
	put_army(orc,(970,380),"500",2) # Goblin Town
	put_army(orc,(930,560),"500",2) # Dimrill Dale
	put_army(orc,(1100,600),"1000",2) # Dol Guldur
	put_army(orc,(1100,600),"1000",2) # Dol Guldur
	put_army(orc,(870,780),"6000",2) # Isengard, 2500 hand orcs, 1500 uruk-hai orcs, 2000 Dunledings
	put_army(elf,(1200,320),"800",1) # Thranduil

	# Mordor armies
	put_army(orc,(conv(38)+20,conv(28.1)),"5000",2) # Mount Doom
	put_army(orc,(conv(37),conv(27)-30),"10000",2) # Morannon
	put_army(orc,(conv(36)+20,conv(30)-30),"10000",2) # Minas Morgul
	put_army(orc,(conv(36)+50,conv(30)-30),"2500",2) # Cirith Ungol
	put_army(orc,(conv(37),conv(27)),"3400",2) # Morannon -> South
	put_army(orc,(conv(40),conv(28)),"9500",2) # Mount Doom
	put_army(troll,(conv(40)+50,conv(28)),"500",2) # Mount Doom
	
	# Rohan armies
	put_army(cavalry,(conv(25.9),conv(24.3)),"120",1)
	put_army(cavalry,(conv(26),conv(26)),"2200",1) # 1200 + 1000 light
	put_army(cavalry,(conv(27.6),conv(26)),"1960",1) # 960 + 1000 light
	put_army(cavalry,(conv(30.2),conv(25.7)),"120",1) # Eomer
	
	# Dol Amroth, Isildur
	put_army(infantry,(conv(27.6),conv(31.2)),"1200",1) # 700 men at arms + 500 h
	
	# Gondor
	put_army(infantry,(conv(30.4),conv(32.3)),"500",1) # inf
	put_army(infantry,(conv(33),conv(32.5)),"200",1) # inf
	put_army(infantry,(conv(34.5)+40,conv(27.3)+10),"200",1) # Faramir
	put_army(infantry,(conv(34)+30,conv(28.1)+30),"2200",1) # 100 inf + 1500 inf + 100 tower guards + 100 inf + 400 inf

	# Dwarves
	put_army(dwarf,(conv(36.6),conv(9.2)),"1000",1)
	put_army(dwarf,(conv(41.2),conv(9.7)),"500",1)
	
	# Bard
	put_army(infantry,(conv(36.7),conv(10.2)),"400",1)

        if image_w < view_size[0] or image_h < view_size[1]:
            print ("The source image is too small for this example.")
            print ("A %i by %i or larger image is required." % zoom_view_size)
            return

        regions = pygame.Surface(win_size, 0, 24)
        add_arrow_button(screen, regions,
                         (40, win_size[1] // 2), DIR_LEFT)
        add_arrow_button(screen, regions,
                         (win_size[0] - 40, win_size[1] // 2), DIR_RIGHT)
        add_arrow_button(screen, regions,
                         (win_size[0] // 2, 40), DIR_UP)
        add_arrow_button(screen, regions,
                         (win_size[0] // 2, win_size[1] - 40), DIR_DOWN)
        pygame.display.flip()

        screen.set_clip((margin, margin, zoom_view_size[0], zoom_view_size[1]))

        view_rect = Rect(0, 0, view_size[0], view_size[1])

        scale(image.subsurface(view_rect), zoom_view_size,
              screen.subsurface(screen.get_clip()))
        pygame.display.flip()


        # the direction we will scroll in.
        direction = None

        clock = pygame.time.Clock()
        clock.tick()

        going = True
        while going:
            # wait for events before doing anything.
            #events = [pygame.event.wait()] + pygame.event.get()
            events = pygame.event.get()

            for e in events:
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        going = False
                    elif e.key == K_DOWN:
                        scroll_view(screen, image, DIR_DOWN, view_rect)
                    elif e.key == K_UP:
                        scroll_view(screen, image, DIR_UP, view_rect)
                    elif e.key == K_LEFT:
                        scroll_view(screen, image, DIR_LEFT, view_rect)
                    elif e.key == K_RIGHT:
                        scroll_view(screen, image, DIR_RIGHT, view_rect)
                elif e.type == QUIT:
                    going = False
                elif e.type == MOUSEBUTTONDOWN:
                    direction = regions.get_at(e.pos)[0]
                elif e.type == MOUSEBUTTONUP:
                    direction = None

            if direction:
                scroll_view(screen, image, direction, view_rect)

            clock.tick(30)

    finally:
        pygame.key.set_repeat (old_k_delay, old_k_interval)
        pygame.quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        image_file = sys.argv[1]
    else:
        image_file = None
    main(image_file)
