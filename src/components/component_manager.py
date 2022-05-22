class ComponentManager():
    def __init__(self, components):
        self.components = components

    def add(self, component):
        if component not in self.components:
            self.components.append(component)