import pygame
import random
import math
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.button import Button


dif_rate = 0.05
start_n = - 1


class Ball(Widget):
    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
    
    def draw(self, game):
        with game.canvas.after:
            Color(255, 69, 0, 0.7)
            self.flame_1 = Ellipse(size=(9, 9), pos=(Window.width / 2 + 4, 
                                                Window.height / 2 + 4))
            Color(255, 69, 0, 0.6)
            self.flame_2 = Ellipse(size=(8, 8), pos=(Window.width / 2 + 7, 
                                                Window.height / 2 + 7))
            Color(255, 69, 0, 0.5)
            self.flame_3 = Ellipse(size=(7, 7), pos=(Window.width / 2 + 10, 
                                                Window.height / 2 + 10))
            Color(255, 69, 0, 0.4)
            self.flame_4 = Ellipse(size=(6, 6), pos=(Window.width / 2 + 13, 
                                                Window.height / 2 + 13))
            Color(255, 69, 0, 0.3)
            self.flame_5 = Ellipse(size=(5, 5), pos=(Window.width / 2 + 16, 
                                                Window.height / 2 + 16))
            Color(255, 69, 0, 0.2)
            self.flame_6 = Ellipse(size=(4, 4), pos=(Window.width / 2 + 19, 
                                                Window.height / 2 + 19))


class Star(Widget):
    def __init__(self, **kwargs):
        super(Star, self).__init__(**kwargs)
        self.starlist = []

    def draw(self, game):
        for times in range(50):
            pos_x = random.randrange(0, Window.width)
            pos_y = random.randrange(0, Window.height)
            with game.canvas:
                Color(200, 255, 255, 0.5)
                self.star_times = Rectangle(source='star.png', pos=(pos_x, pos_y), size=(6, 6))
                self.starlist.append(self.star_times)


class Planet(Widget):
    def __init__(self, **kwargs):
        super(Planet, self).__init__(**kwargs)

    def draw(self, game):
        pos_x = random.randrange(0, Window.width)
        pos_y = random.randrange(0, Window.height)
        with game.canvas:
            Color(0, 0, 0.6, 1)
            self.rect_1 = Rectangle(source='planet.png', size=(166, 168), pos=(pos_x, pos_y))


class Meteorites(Widget):
    def __init__(self, **kwargs):
        super(Meteorites, self).__init__(**kwargs)
        self.meteolist = []
        self.meteolist_ini = []
    
    def draw(self, game):
        for times in range(3):
            randNum = random.randint(1, 4)
            if randNum == 1:
                pos_x = random.randrange(1, Window.width - 1)
                pos_y = (- 20)
            elif randNum == 2:
                pos_x = (- 20)
                pos_y = random.randrange(1, Window.height - 1)
            elif randNum == 3:
                pos_x = random.randrange(1, Window.width - 1)
                pos_y = Window.height + 20
            else:
                pos_x = Window.width + 20
                pos_y = random.randrange(1, Window.height - 1)
            with game.canvas:
                Color(1, 0, 0.3, 0.6)
                self.meteo_times = Rectangle(source='sandstone_2.png',size=(20, 20), pos=(pos_x, pos_y))
                self.meteolist.append(self.meteo_times)
                Color(1, 0, 0.3, 0)
                self.meteo_times_ini = Rectangle(size=(20, 20), pos=(pos_x, pos_y))
                self.meteolist_ini.append(self.meteo_times_ini)


class Survival(Widget):
    # ball = ObjectProperty(None)
    # star = ObjectProperty(None)
    # planet = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Survival, self).__init__(**kwargs)
        self.ball = Ball()
        self.planet = Planet()
        self.star = Star()
        self.meteorites = Meteorites()
        self.ball.draw(self)
        self.star.draw(self)
        self.planet.draw(self)
        self.meteorites.draw(self)

        Clock.schedule_interval(self.move, 0)
        Clock.schedule_interval(self.show_time, 0.1)
        Clock.schedule_interval(self.gameover, 0)

    def move(self, *l):
        global start_n
        t = Clock.get_boottime()
        # Direction of Movement
        # Upper Right Quadrant
        if Window.mouse_pos[0] >= (Window.width / 2) and Window.mouse_pos[1] >= (Window.height / 2):
            a = - (Window.mouse_pos[1] - Window.height / 2)
            b = - (Window.mouse_pos[0] - Window.width / 2)
        # Upper Left Quadrant
        elif Window.mouse_pos[0] <= (Window.width / 2) and Window.mouse_pos[1] >= (Window.height / 2):
            a = - (Window.mouse_pos[1] - Window.height / 2)
            b =  Window.width / 2 - Window.mouse_pos[0]
        # Lower Left Quadrant
        elif Window.mouse_pos[0] <= (Window.width / 2) and Window.mouse_pos[1] <= (Window.height / 2):
            a = Window.height / 2 - Window.mouse_pos[1]
            b = Window.width / 2 - Window.mouse_pos[0]
        # Lower Right Quadrant
        elif Window.mouse_pos[0] >= (Window.width / 2) and Window.mouse_pos[1] <= (Window.height / 2):
            a = Window.height / 2 - Window.mouse_pos[1]
            b = - (Window.mouse_pos[0] - Window.width / 2)
        bottom = abs(a) + abs(b)
        x_rate = b / bottom
        y_rate = a / bottom

        # Move the ball's tail
        self.ball.flame_1.pos = (4 * x_rate + Window.width / 2,
                                 4 * y_rate + Window.height / 2)
        self.ball.flame_2.pos = (7 * x_rate + Window.width / 2,
                                 7 * y_rate + Window.height / 2)
        self.ball.flame_3.pos = (10 * x_rate + Window.width / 2,
                                 10 * y_rate + Window.height / 2)
        self.ball.flame_4.pos = (13 * x_rate + Window.width / 2,
                                 13 * y_rate + Window.height / 2)
        self.ball.flame_5.pos = (16 * x_rate + Window.width / 2,
                                 16 * y_rate + Window.height / 2)
        self.ball.flame_6.pos = (19 * x_rate + Window.width / 2,
                                 19 * y_rate + Window.height / 2)
        # Move the planet
        self.planet.rect_1.pos = (dif_rate * x_rate * t + self.planet.rect_1.pos[0],
                                  dif_rate * y_rate * t + self.planet.rect_1.pos[1])
        # When it goes out of the screen 
        if self.planet.rect_1.pos[0] > Window.width + self.planet.rect_1.size[0]:
            self.planet.rect_1.pos = (0 - self.planet.rect_1.size[0],
                                      random.randrange(0, Window.height))
        elif self.planet.rect_1.pos[0] < 0 - self.planet.rect_1.size[0]:
            self.planet.rect_1.pos = (Window.width + self.planet.rect_1.size[0],
                                      random.randrange(0, Window.height))
        elif self.planet.rect_1.pos[1] > Window.height + self.planet.rect_1.size[1]:
            self.planet.rect_1.pos = (random.randrange(0, Window.width),
                                      0 - self.planet.rect_1.size[1])
        elif self.planet.rect_1.pos[1] < 0 - self.planet.rect_1.size[1]:
            self.planet.rect_1.pos = (random.randrange(0, Window.width),
                                      Window.height + self.planet.rect_1.size[1])

        # Move the stars
        for item in self.star.starlist:
            item.pos = (dif_rate * x_rate * t + item.pos[0], 
                        dif_rate * y_rate * t + item.pos[1])
            # When it goes out of the screen 
            if item.pos[0] >= Window.width + item.size[0]:
                item.pos = (0 - item.size[0], random.randrange(0, Window.height))
            elif item.pos[0] <= 0 - item.size[0]:
                item.pos = (Window.width + item.size[0], random.randrange(0, Window.height))
            elif item.pos[1] >= Window.height + item.size[1]:
                item.pos = (random.randrange(0, Window.width), 0 - item.size[1])
            elif item.pos[1] <= 0 - item.size[1]:
                item.pos = (random.randrange(0, Window.width), Window.height + item.size[1])
        
        # Move the meteorites
        # Move the meteorites along with the background
        for item in self.meteorites.meteolist:
            item.pos = (dif_rate * x_rate * t + item.pos[0], 
                        dif_rate * y_rate * t + item.pos[1])
        # When it goes out of the screen
            if start_n == 2:
                start_n = - 1
            start_n += 1
            if (item.pos[0] > Window.width + item.size[0] or 
                item.pos[0] < 0 - item.size[0] or
                item.pos[1] > Window.height + item.size[1] or
                item.pos[1] < 0 - item.size[1]):
                random_N = random.randint(1, 4)
                if random_N == 1: # from BOTTOM
                    item.pos = (random.randrange(1, Window.width - 1), 0 - item.size[1])
                    self.meteorites.meteolist_ini[start_n].pos = item.pos
                elif random_N == 2: # from LEFT
                    item.pos = (0 - item.size[0], random.randrange(1, Window.height - 1))
                    self.meteorites.meteolist_ini[start_n].pos = item.pos
                elif random_N == 3: # from TOP
                    item.pos = (random.randrange(1, Window.width - 1), Window.height + item.pos[1])
                    self.meteorites.meteolist_ini[start_n].pos = item.pos
                else: # from RIGHT
                    item.pos = (Window.width + item.size[0], random.randrange(1, Window.height - 1))
                    self.meteorites.meteolist_ini[start_n].pos = item.pos
        # Move the metorites in straight paths
        for item in self.meteorites.meteolist_ini:
            if start_n == 2:
                start_n = - 1
            start_n += 1
            # Upper Right Quadrant
            if item.pos[0] >= (Window.width / 2) and item.pos[1] == Window.height + 20:
                x = - (item.pos[0] - (Window.width / 2))
                y = - (Window.height / 2 + 20)
            elif item.pos[0] == Window.width + 20 and item.pos[1] >= (Window.height / 2):
                x = - (Window.width / 2 + 20)
                y = - (item.pos[1] - (Window.height / 2))
            # Upper Left Quadrant
            elif item.pos[0] <= (Window.width / 2) and item.pos[1] == Window.height + 20:
                x = (Window.width / 2) - item.pos[0]
                y = - (Window.height / 2 + 20)
            elif item.pos[0] == (- 20) and item.pos[1] >= (Window.height / 2):
                x = (Window.width / 2 + 20)
                y = - (item.pos[1] - (Window.height / 2))
            # Lower Left Quadrant
            elif item.pos[0] == (- 20) and item.pos[1] <= (Window.height / 2):
                x = (Window.width / 2 + 20)
                y = (Window.height / 2) - item.pos[1]
            elif item.pos[0] <= (Window.width / 2) and item.pos[1] == (- 20):
                x = (Window.width / 2) - item.pos[0]
                y = (Window.height / 2 + 20)
            # Lower Right Quadrant
            elif item.pos[0] >= (Window.width / 2) and item.pos[1] == (- 20):
                x = - item.pos[0] - (Window.width / 2)
                y = (Window.height / 2 + 20)
            else:
                x = - (Window.width / 2 + 20)
                y = (Window.height / 2) - item.pos[1]
            bottom_new = abs(x) + abs(y)
            x_rate_new = x / bottom_new
            y_rate_new = y / bottom_new
            self.meteorites.meteolist[start_n].pos = (6 * dif_rate * x_rate_new * t + self.meteorites.meteolist[start_n].pos[0], 
                                                      6 * dif_rate * y_rate_new * t + self.meteorites.meteolist[start_n].pos[1])
    
    def show_time(self, *l):
        with self.canvas:
            self.button = Button(pos=(Window.width - 160, Window.height - 90), size=(100, 60))
        self.button.background_color = (1,0.3,0.3,0.7)
        self.button.text += str(round(Clock.get_boottime(), 3))

    # def again(self, *l):
    #     self.canvas.clear()
    #     Clock.unschedule(self.gameover)
    #     Clock.schedule_interval(self.show_time)
    #     Clock.schedule_interval(self.move)

    def end_screen(self, *l):
        Clock.unschedule(self.show_time)
        Clock.unschedule(self.move)
        with self.canvas:
            label_end = Label(text='[i]Time of Survival: %s Seconds[/i]' % (self.button.text), markup = True,
                              pos=(Window.width / 2, Window.height / 3 * 2), size=(0, 0))
            again_button = Button(pos=(Window.width / 2 - 80, Window.height / 3), size=(160, 50))
        again_button.background_color = (0,1,1,0.7)
        again_button.text += 'Play Again'
        # again_button.bind(on_press=again())
        label_end.font_size = 30
        label_end.font_name = 'Arial'

    def gameover(self, *l):
        for times in range(3):
            if (self.meteorites.meteolist[times].pos[0] + 16 >= (Window.width / 2 + 8) and
                self.meteorites.meteolist[times].pos[1] + 16 >= (Window.height / 2 + 8) and
                self.meteorites.meteolist[times].pos[0] - 16 <= (Window.width / 2 - 8) and
                self.meteorites.meteolist[times].pos[1] - 16 <= (Window.height / 2 - 8)):
                self.end_screen()



class SurvivalApp(App):
    def build(self):
        game = Survival()
        return game


if __name__ == '__main__':
    SurvivalApp().run()
