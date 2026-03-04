import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


def query(sql: str) -> pd.DataFrame:
    return pd.read_sql(sql, engine)


def get_all_stats() -> pd.DataFrame:
    sql = """
    SELECT 
        se.id,
        se.type,
        se.context,
        se."shotOutcome",
        se.period,
        se.clock,
        se.x,
        se.y,
        se."goalX",
        se."goalY",
        se.timestamp,
        p.id as player_id,
        p.name as player_name,
        g.id as game_id,
        g.opponent,
        g.date as game_date,
        g."teamScore",
        g."opponentScore",
        gr."capNumber" as cap_number
    FROM "StatEvent" se
    JOIN "Player" p ON se."playerId" = p.id
    JOIN "Game" g ON se."gameId" = g.id
    LEFT JOIN "GameRoster" gr ON gr."gameId" = g.id AND gr."playerId" = p.id
    ORDER BY se.timestamp
    """
    return query(sql)


def get_games() -> pd.DataFrame:
    sql = """
    SELECT 
        id,
        opponent,
        date,
        status,
        "teamScore",
        "opponentScore"
    FROM "Game"
    ORDER BY date DESC
    """
    return query(sql)


def get_players() -> pd.DataFrame:
    sql = """
    SELECT 
        id,
        name,
        "firstName",
        "lastName"
    FROM "Player"
    """
    return query(sql)

def get_player_summary() -> pd.DataFrame:
    sql = """
    SELECT 
        p.name as player_name,
        COUNT(*) FILTER (WHERE se.type = 'GOAL') as goals,
        COUNT(*) FILTER (WHERE se.type = 'ASSIST') as assists,
        COUNT(*) FILTER (WHERE se.type = 'STEAL') as steals,
        COUNT(*) FILTER (WHERE se.type = 'BLOCK') as blocks,
        COUNT(*) FILTER (WHERE se.type = 'EXCLUSION') as exclusions,
        COUNT(*) FILTER (WHERE se.type = 'TURNOVER') as turnovers,
        COUNT(*) FILTER (WHERE se.type = 'SAVE') as saves
    FROM "Player" p
    LEFT JOIN "StatEvent" se ON se."playerId" = p.id
    GROUP BY p.id, p.name
    ORDER BY goals DESC
    """
    return query(sql)

def get_game_summary(game_id: int) -> pd.DataFrame:
    sql = f"""
    SELECT 
        p.name as player_name,
        gr."capNumber" as cap,
        COUNT(*) FILTER (WHERE se.type = 'GOAL') as goals,
        COUNT(*) FILTER (WHERE se.type = 'ASSIST') as assists,
        COUNT(*) FILTER (WHERE se.type = 'STEAL') as steals,
        COUNT(*) FILTER (WHERE se.type = 'EXCLUSION') as exclusions
    FROM "GameRoster" gr
    JOIN "Player" p ON gr."playerId" = p.id
    LEFT JOIN "StatEvent" se ON se."playerId" = p.id AND se."gameId" = {game_id}
    WHERE gr."gameId" = :game_id
    GROUP BY p.id, p.name, gr."capNumber"
    ORDER BY gr."capNumber"
    """

    return pd.read_sql(sql, engine, params={"game_id": game_id})

def get_shots() -> pd.DataFrame:
    sql = """
    SELECT 
        se.x,
        se.y,
        se."goalX",
        se."goalY",
        se."shotOutcome",
        se.context,
        se.period,
        se.clock,
        p.name as player_name,
        g.id as game_id
    FROM "StatEvent" se
    JOIN "Player" p ON se."playerId" = p.id
    JOIN "Game" g ON se."gameId" = g.id
    WHERE se.type IN ('GOAL', 'SHOT')
    ORDER BY se.timestamp
    """
    return query(sql)