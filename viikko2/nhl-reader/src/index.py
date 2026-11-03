from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table


def main():
    season = Prompt.ask("Kausi")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = Prompt.ask("Kansalaisuus").strip().upper()
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Kauden {season} pelaajat maasta {nationality}")

    table.add_column("Pelaaja", style="cyan")
    table.add_column("Joukkueet", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()