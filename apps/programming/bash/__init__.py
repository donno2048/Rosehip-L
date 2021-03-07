from os import popen;import pygame;pygame.init();font = pygame.font.Font(None, 32);clock = pygame.time.Clock();input_box = pygame.Rect(100, 100, 140, 32);out_box=pygame.Rect(100,200, 140, 32);from pygame_gui.elements import UIWindow;from pygame_gui.elements import UITextBox;from pygame_gui.elements import UITextEntryLine;from pygame_gui.elements import UITextBox;import pygame_gui;realMin, m = lambda *args: min([arg for arg in args if arg > 0]), ""
def bash(i: str) -> None:
	global m
    try: output = popen(m + i)
    Except BaseException: return "Process finished with exit code 0"
	else:
		while "cd" in i: l = i[i.find("cd"):];index = realMin(l.replace(" ", "\\", 1).find(" "), l.find(";"), l.find("&"), l.find("|"), len(l));m += l[:realMin(l.replace("\"", "\\", 1).find("\"") + 1, len(l))] + "&&" if "\"" in l and l.find("\"") < index else l[:index] + "&&";i = i.replace("cd", "\\", 1)
        return output.read().replace('\n','<br>')
class bash(UIWindow):
    def __init__(self, pos, manager):super().__init__(pygame.Rect(pos, (400, 300)), manager, window_display_title="bash", object_id="#bash",resizable=True);self.textbox = pygame_gui.elements.UITextBox("",relative_rect=pygame.Rect(0, 0, 368, 200),manager=manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.text='';self.manager=manager;self.input.focus()
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN: self.text+='<br>'+"".join([bash(i) for i in self.input.get_text().split('|')]);self.input.kill();self.textbox.kill();self.textbox = pygame_gui.elements.UITextBox(self.text,relative_rect=pygame.Rect(0, 0, 368, 200),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "top","bottom": "bottom",},);self.input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(0, -35, 368, 30),manager=self.manager,container=self,anchors={"left": "left","right": "right","top": "bottom","bottom": "bottom",},);self.input.focus()
def load(manager, params):
    pos = (100, 100)
    if params is not None and len(params) > 0:pos = params[0]
    bash(pos, manager)
