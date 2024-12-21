"""
create order table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
            """
            create extension if not exists "uuid-ossp"; -- for generating uuid4
            
            create table if not exists users (
                id text primary key default uuid_generate_v4(),
                username text not null,
                password text not null,
                created_at timestamp default now(),
                deleted_at timestamp
            );
        """,
        """
            drop table if exists users;
        """
    ),
    step(
        """
            create unique index if not exists unique_username_active
            on users (username)
            where deleted_at is null;
        """,
        """
            drop index if exists unique_username_active;
        """
    )
]
