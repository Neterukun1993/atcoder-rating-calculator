"""
Calculator of Atcoder rating
Reference: https://www.dropbox.com/s/ixci4amralioaif/rating.pdf
"""

import math


Performance = int


class RateCalculator:
    def __init__(self) -> None:
        self.perfs: list[Performance] = []

    def add(self, perf: Performance) -> None:
        self.perfs.append(perf)

    def _correction(self) -> float:
        def F(count: int) -> float:
            numer = math.sqrt(sum(0.81 ** i for i in range(1, count + 1)))
            denom = sum(0.9 ** i for i in range(1, count + 1))
            return numer / denom

        def F_INF() -> float:
            numer = math.sqrt(0.81 / (1 - 0.81))
            denom = 0.9 / (1 - 0.9)
            return numer / denom

        numer = F(len(self.perfs)) - F_INF()
        denom = F(1) - F_INF()
        return 1200 * numer / denom

    def _rate(self) -> float:
        numer = sum(2 ** (perf / 800) * (0.9 ** i) for i, perf in enumerate(reversed(self.perfs), 1))
        denom = sum(0.9 ** i for i in range(1, len(self.perfs) + 1))
        return 800 * math.log2(numer / denom)

    @property
    def rate(self) -> int:
        return int(self._rate() - self._correction())


def main() -> None:
    perfs_from_oldest_to_newest = [400, 800, 600, 1000, 1200]
    rc = RateCalculator()
    for perf in perfs_from_oldest_to_newest:
        rc.add(perf)
    print(rc.rate)


if __name__ == "__main__":
    main()
