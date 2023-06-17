from pipeline.mods.videolist import VideoList
from pipeline.mods.step import StepException
from pipeline.pipeline import Pipeline

CHANNEL_ID = "UCMki_UkHb4qSc0qyEcOHHJw"


def main():
    inputs = {
        "channel_id": CHANNEL_ID
    }  # parameter in "process"

    steps = [
        VideoList(),
    ]  # classes

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
