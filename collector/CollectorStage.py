from data.collector.accumulators import Accumulate
from data.collector.accumulators.ClassRegistry import CLASS_REGISTRY

class CollectorStage:
    def __init__(self, config: list[dict]):
        self._accumulators = self._gatherAccs(config)

    @property
    def accumulators(self) -> list[Accumulate]:
        return self._accumulators

    @accumulators.setter
    def accumulators(self, config: list[dict]) -> None:
        self._accumulators = self._gatherAccs(config)

    def execute(self) -> None:
        for acc in self._accumulators:
            acc.execute()

    def _gatherAccs(self, config: list[dict]) -> list[Accumulate]:
        return [
            CLASS_REGISTRY[config["name"]](**config["params"])
        ]



