from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    
    query = QueryBuilder()
    
    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
    .playsIn("EDM")
    .hasAtLeast(50, "points")
    .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
