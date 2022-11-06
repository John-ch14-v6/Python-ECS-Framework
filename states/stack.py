from entities.entity_pool import POOL
from scripts.components import AddState, PopState


class StateStack:
    def __init__(self):
        self.states = {

        }
        self.stack = []

    def start(self):
        # self.stack.append(self.states['splash']())
        self.stack[-1].activate()
        self.stack[-1].start()

    def update(self):
        if change := POOL.grab(PopState):
            self.remove_state()
            change.remove(PopState)

        if change := POOL.grab(AddState):
            new_state = change.get(AddState).state
            change.remove(AddState)
            self.add_state(new_state)

    def add_state(self, new_state):
        self.stack[-1].deactivate()
        self.stack.append(self.states[new_state]())
        self.stack[-1].activate()
        self.stack[-1].start()

    def remove_state(self):
        self.stack[-1].deactivate()
        self.stack.pop(-1)
        self.stack[-1].activate()


STATE_STACK = StateStack()
