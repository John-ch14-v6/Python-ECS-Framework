class EntityPool:
    def __init__(self):
        self.entities = []

    def add(self, entities):
        entities = [[entities], entities][type(entities) == list]
        for entity in entities:
            self.entities.append(entity)

    def remove(self, entities):
        entities = [[entities], entities][type(entities) == list]
        for entity in entities:
            self.entities.remove(entity)

    def grab(self, components: list):
        if entities := self.get(components):
            return entities[0]

    def get(self, components: list):
        return [entity for entity in self.entities if bool(entity.has(components))]


POOL = EntityPool()
