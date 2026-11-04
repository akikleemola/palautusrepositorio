from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def hae_otsikko(season, search_type, search_value):
    if search_type == "kansalaisuus":
        return f"Kauden {season} pelaajat maasta {search_value}"
    return f"Kauden {season} joukkueen {search_value} pelaajat"


def lisaa_sarakkeet(table):
    table.add_column("Pelaaja", style="cyan")
    table.add_column("Joukkueet", style="magenta")
    table.add_column("Maalit", justify="right", style="green")
    table.add_column("Syötöt", justify="right", style="green")
    table.add_column("Pisteet", justify="right", style="green")


def luo_taulukko(season, search_type, search_value):
    table = Table(title=hae_otsikko(season, search_type, search_value))
    lisaa_sarakkeet(table)
    return table


def lisaa_pelaaja(table, player):
    table.add_row(
        player.name,
        player.team,
        str(player.goals),
        str(player.assists),
        str(player.goals + player.assists)
    )


def tulosta_pelaajat(players, season, search_type, search_value):
    table = luo_taulukko(season, search_type, search_value)

    for player in players:
        lisaa_pelaaja(table, player)

    console = Console()
    console.print(table)


def hae_pelaajat(stats, search_type, search_value):
    if search_type == "kansalaisuus":
        return stats.top_scorers_by_nationality(search_value)
    return stats.top_scorers_by_team(search_value)


def main():
    season = Prompt.ask("Kausi")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    search_type = Prompt.ask("Haku", choices=["kansalaisuus", "joukkue"])
    prompt = "Kansalaisuus" if search_type == "kansalaisuus" else "Joukkue"
    search_value = Prompt.ask(prompt).strip().upper()
    players = hae_pelaajat(stats, search_type, search_value)

    tulosta_pelaajat(players, season, search_type, search_value)


if __name__ == "__main__":
    main()
