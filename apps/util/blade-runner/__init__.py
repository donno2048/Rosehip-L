import pygame
screen = pygame.display.set_mode((1024, 600))
import pygame_gui
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_window import UIWindow
from pygame_gui.elements.ui_image import UIImage
from blade_runner import load, play
class PongWindow(UIWindow):
    def __init__(self, position, ui_manager):
        super().__init__(pygame.Rect(position, (320, 240)), ui_manager, object_id='#window')
        game_surface_size = self.get_container().get_size()
        self.game_surface_element = UIImage(pygame.Rect((0, 0), game_surface_size), pygame.Surface(game_surface_size).convert(), manager=ui_manager, container=self, parent_element=self)
    def process_event(self, event):
        handled = super().process_event(event)
        if (event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#window.#title_bar" and event.ui_element == self.title_bar):
            handled = True
            event_data = {'user_type': 'pong_window_selected', 'ui_element': self, 'ui_object_id': self.most_specific_combined_id}
            window_selected_event = pygame.event.Event(pygame.USEREVENT, event_data)
            pygame.event.post(window_selected_event)
        return handled
    def update(self, time_delta):
        if self.alive(): play()
        super().update(time_delta)
class MiniGamesApp:
    def __init__(self, size, screen = screen):
        pygame.init()
        self.root_window_surface = screen
        self.background_surface = pygame.Surface((1024, 600)).convert()
        self.background_surface.fill(pygame.Color('#505050'))
        self.ui_manager = UIManager((1024, 600))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.window = PongWindow((25, 25), self.ui_manager)
        load(size, self.window.game_surface_element.image)
    def run(self):
        while self.is_running:
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.ui_manager.process_events(event)
            self.ui_manager.update(time_delta)
            self.root_window_surface.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.root_window_surface)
            pygame.display.update()
def load(manager, params): MiniGamesApp((600, 400), manager).run()