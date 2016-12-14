
class ViewBackground:

    @staticmethod
    def fill_view(background, color):
        background.fill(color)

    @staticmethod
    def blit_view(window, image, x, y):
        window.blit(image, (x, y))

    @staticmethod
    def blit_font(background,font,text,value,color,x,y):
        background.blit(font.render(text, value, color), (x, y))
        pass