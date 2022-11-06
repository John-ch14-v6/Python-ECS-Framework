from dataclasses import dataclass


@dataclass(slots=True)
class Component:
    pass


@dataclass(slots=True)
class Close(Component):
    pass


@dataclass(slots=True)
class AddState(Component):
    state:      str


@dataclass(slots=True)
class PopState(Component):
    pass
