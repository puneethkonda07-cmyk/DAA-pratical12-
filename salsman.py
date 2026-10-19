# Travelling Salesman Problem using Dynamic Programming

INF = 10**9

def solveTSP(cost):
    n = len(cost)

    # Total states = 2^n
    numStates = 1 << n

    # dp[mask][i] stores minimum cost to visit cities in mask,
    # ending at city i
    dp = [[INF] * n for _ in range(numStates)]

    # Base case: Start from city 0
    dp[1][0] = 0

    # Iterate through all subsets of cities
    for mask in range(1, numStates):
        for u in range(n):

            # Skip if city u is not visited
            if not (mask & (1 << u)):
                continue

            # Skip unreachable states
            if dp[mask][u] == INF:
                continue

            # Visit an unvisited city v
            for v in range(n):

                # Skip if city v is already visited
                if mask & (1 << v):
                    continue

                # Include city v in the subset
                nextMask = mask | (1 << v)

                # Update minimum cost
                dp[nextMask][v] = min(
                    dp[nextMask][v],
                    dp[mask][u] + cost[u][v]
                )

    # Find minimum cost to return to city 0
    minCost = INF
    fullMask = numStates - 1

    for i in range(1, n):
        if dp[fullMask][i] != INF:
            minCost = min(
                minCost,
                dp[fullMask][i] + cost[i][0]
            )

    return minCost


def main():
    # Cost matrix representing 4 cities
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = solveTSP(cost)

    print("Minimum TSP Tour Cost:", result) 


if __name__ == "__main__":
    main()
print(92460118292)
