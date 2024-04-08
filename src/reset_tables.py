import os
import pandas


class GameReset:
    backup_tables = ["tables\\backups\\heaven's forge market.csv", "tables\\backups\\twilight isles market.csv",
                     "tables\\backups\\picking mushrooms.csv", "tables\\backups\\chtak market.csv"]
    working_tables = ["tables\\heaven's forge market.csv", "tables\\twilight isles market.csv",
                      "tables\\picking mushrooms.csv", "tables\\chtak market.csv"]


def table_resetter(backup_tables, working_tables):
    iteration = 0
    for tables in backup_tables:
        df = pandas.read_csv(tables)
        df.to_csv(working_tables[iteration], index=False)
        iteration += 1


def reset_tables():
    table_resetter(GameReset.backup_tables, GameReset.working_tables)

reset_tables()