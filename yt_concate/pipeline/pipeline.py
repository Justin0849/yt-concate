from .mods.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:  # set up the instances
            try:
                step.process(inputs)

            except StepException as e:
                print(e)
                break
