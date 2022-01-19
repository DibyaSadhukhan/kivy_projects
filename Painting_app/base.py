from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color , Ellipse ,Line

class Paint_Widget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1.,1.,0)
            touch.ud['line']=Line(points=(touch.x,touch.y))
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]

class Paint_App(App):
    def build(self):
        return Paint_Widget()

if __name__=='__main__':
    Paint_App().run()
