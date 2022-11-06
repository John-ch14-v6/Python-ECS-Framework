class Entity:
    def __init__(self):
        self.components = {}

    def add(self, components):
        components = [[components], components][type(components) == list]

        for component in components:
            self.components[type(component)] = component

    def remove(self, component_type):
        return bool(self.components.pop(component_type))

    def get(self, component_type):
        return self.components.get(component_type, False)

    def has(self, components_list):
        return not (False in [self.get(component) for component in components_list])
