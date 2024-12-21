"""Automatically truncate all tables before each test."""

import pytest

from app.internal.repository.postgresql.connection import get_connection


async def __clean_postgres():
    """Truncate all tables (except yoyo migrations) before each test."""

    q = """
        CREATE OR REPLACE FUNCTION truncate_tables() RETURNS void AS $$
        DECLARE
            statements CURSOR FOR
                SELECT tablename FROM pg_tables
                WHERE schemaname = 'public'
                    and tablename not like '%yoyo%'
                    and tablename not like 'user_roles';
        BEGIN
            FOR stmt IN statements LOOP
                EXECUTE 'TRUNCATE TABLE ' || quote_ident(stmt.tablename) || ' CASCADE;';
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """

    async with get_connection() as cur:
        await cur.execute(q)
        await cur.execute("select truncate_tables();")


@pytest.fixture(autouse=True, scope="module")
async def auto_clean_postgres():
    """Automatically clean postgres before each test module."""

    await __clean_postgres()


@pytest.fixture()
async def clean_postgres():
    """Clean postgres."""
    await __clean_postgres()
