from typing import Any, Dict, Iterable, Union

from sqlalchemy.schema import Table

from app.infra.database.sqlalchemy import metadata

ValuesType = Dict[str, Any]


def insert_model(model: Table, values: Union[ValuesType, Iterable[ValuesType]]) -> None:
    query = model.insert()
    if isinstance(values, Dict):
        metadata.bind.execute(query, **values)
    else:
        metadata.bind.execute(query, list(values))
