import logging
from typing import Any, Awaitable, Callable, Dict, Iterable

from databases import Database
from sqlalchemy.schema import Table

from app.infra.database.sqlalchemy import (
    database_context,
    init_database,
    truncate_database,
)

SeedFn = Callable[[Database], Awaitable[None]]

logger = logging.getLogger(__name__)
seeds: Iterable[SeedFn] = []


async def _populate_table(
    db: Database, table: Table, values: Iterable[Dict[str, Any]],
):
    name: str = table.name
    query = table.insert()

    logger.info(f"Seeding table {name}")
    await db.execute_many(query, list(values))
    logger.info(f"Seeded table {name} successfully")


async def run() -> None:
    logger.info("Initializing databases")
    init_database()
    async with database_context() as database:
        logger.info("Truncating database")
        await truncate_database()
        logger.info("Populating database")
        for fn in seeds:
            await fn(database)
        logger.info("Finished populating PostgreSQL database")
