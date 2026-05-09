class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = set(preconditions)
        self.effects = set(effects)


class PlanningGraph:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = set(initial_state)
        self.goal_state = set(goal_state)
        self.actions = actions

    def generate_plan(self):
        current_state = self.initial_state.copy()
        plan = []

        while not self.goal_state.issubset(current_state):
            action_applied = False

            for action in self.actions:
                if action.preconditions.issubset(current_state):
                    if not action.effects.issubset(current_state):
                        current_state.update(action.effects)
                        action_applied = False
                        plan.append(action.name)
                        action_applied = True

            if not action_applied:
                return None

        return plan