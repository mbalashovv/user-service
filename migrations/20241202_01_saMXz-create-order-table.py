"""
create order table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        create table if not exists users (
            id serial primary key not null,
            username text not null,
            password text not null,
            created_at timestamp default now(),
            deleted_at timestamp
        );
    """,
    """
        drop table if exists users;
    """)
]
