import math


def best_strategy(data: tuple, strategies: tuple) -> tuple:
    results = [strategy(data) for strategy in strategies]
    max_index = results.index(max(results))
    return strategies[max_index], results[max_index]


def worst_strategy(data: tuple, strategies: tuple) -> tuple:
    results = [strategy(data) for strategy in strategies]
    min_index = results.index(min(results))
    return strategies[min_index], results[min_index]


def main() -> None:
    data = tuple(i for i in range(1, 10))

    arithmetic_mean = lambda nums: sum(nums) / len(nums)
    geometric_mean = lambda nums: math.prod(nums) ** (1 / len(nums) if all(j >= 0 for j in data) else float("-inf"))
    harmonic_mean = lambda nums: len(nums) / sum((1 / i) for i in nums if (i != 0)) if all(j != 0 for j in data) else float("-inf")
    rms_mean = lambda data: math.sqrt(sum(x ** 2 for x in data) / len(data))
    median = lambda data: sorted(data)[len(data) // 2] if len(data) % 2 == 1 else (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2
    log_mean = lambda data: math.exp(sum(math.log(x) for x in data) / len(data))

    strategies = (arithmetic_mean, geometric_mean, harmonic_mean, rms_mean, median, log_mean)
    best_method, best_value = best_strategy(data, strategies)
    worst_method, worst_value = worst_strategy(data, strategies)
    best_method_name = [k for k, v in locals().items() if v is best_method][0]
    worst_method_name = [k for k, v in locals().items() if v is worst_method][0]

    for i in range(len(strategies)):
        print(f"  {[k for k, v in locals().items() if v is strategies[i]][0]}:".ljust(18, " "),
              f"{strategies[i](data)}")
    print("╔════════════════════════════════════════════════════════════════════════╗")
    print(f"  Best strategy:   {best_value}, {best_method_name}")
    print(f"  Worst strategy:  {worst_value}, {worst_method_name}")
    print("╚════════════════════════════════════════════════════════════════════════╝")


if __name__ == "__main__":
    main()
