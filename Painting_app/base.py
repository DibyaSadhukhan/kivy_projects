#from playsound import playsound
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color , Line

class Paint_Widget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1.,1.,0)
            touch.ud['line']=Line(points=(touch.x,touch.y))
    def on_touch_move(self, touch):
        #playsound('sounds_tom.wav')
        touch.ud['line'].points += [touch.x,touch.y]

class Paint_App(App):
    def build(self):
        parent = Widget()
        self.painter = Paint_Widget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__=='__main__':
    Paint_App().run()
