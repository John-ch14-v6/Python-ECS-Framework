class System:
    def __init__(self):
        self.subsystems = []

    def start(self):
        for system in self.subsystems:
            system.start()

    def update(self):
        for system in self.subsystems:
            system.update()

    def add_sub(self, system):
        self.subsystems.append(system)

    def remove_sub(self, system):
        self.subsystems.remove(system)


class SubSystem:
    def __init__(self):
        pass

    def start(self):
        pass

    def update(self, *args):
        pass
