from objects.game_object import delete_game_object
from settlers_of_valgard.menu import Menu, MenuAction


class MultiPageMenu(Menu):
    def __init__(self, name, load_contents, on_select, display_item = None, items_per_page = 10, text=None, underline_color="gray") -> None:
        super().__init__(name, text, underline_color)
        self.contents = None
        self.load_contents = load_contents
        self.actions : list[MenuAction] = []
        self.page = 0
        self.items_per_page = items_per_page
        self.on_select = on_select
        self.display_item = display_item or (lambda item : str(item))

    def load(self):
        self.contents = self.load_contents()
        self.max_pages = (len(self.contents) + self.items_per_page - 1) // self.items_per_page
        return super().load()
    
    def build_actions(self) -> list[MenuAction]:
        for action in self.actions:
            delete_game_object(action)
        
        self.actions.clear()

        min_index = self.page * self.items_per_page
        max_index = min(len(self.contents), (self.page + 1) * self.items_per_page)

        for i in range(min_index, max_index):
            self.actions.append(MenuAction(self.display_item(self.contents[i]), lambda : self.on_select(self.contents[i])))

        def set_page(page):
            self.page = page
            self.load()

        if min_index > 0:
            self.actions.append(MenuAction('Previous Page', lambda : set_page(self.page - 1), key='<'))
        if max_index < len(self.contents):
            self.actions.append(MenuAction('Next Page', lambda : set_page(self.page + 1), key='>'))
        
        return self.actions
    
    def get_footer(self):
        footer = super().get_footer() or ''
        return f'Page {self.page + 1} of {self.max_pages}\n{footer}\n'