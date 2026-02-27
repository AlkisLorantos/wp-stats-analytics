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