from pygame import Rect

WIN_WIDTH = 800
WIN_HEIGHT = 640


class LogicCamera:

    @staticmethod
    def in_center(camera, hero):
        camera.window = LogicCamera.camera_configure(camera.window, hero.rect)

    @staticmethod
    def camera_configure(window, hero_rect):
        l, t, _, _ = hero_rect
        _, _, w, h = window
        l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

        l = min(0, l)-32
        l = max(-(window.width - WIN_WIDTH), l)
        t = max(-(window.height - WIN_HEIGHT), t)
        t = min(0, t)

        return Rect(l, t, w, h)