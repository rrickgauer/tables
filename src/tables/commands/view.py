from __future__ import annotations
from tables.domain import models
from .base_command import BaseCommand


class ViewCommand(BaseCommand):
    """Execute a view command."""
    
    def __init__(self, connection: models.DatabaseConnection):
        self._connection = connection
