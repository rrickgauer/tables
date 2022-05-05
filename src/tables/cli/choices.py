from __future__ import annotations
from tables.domain.views import SqlColumnDescription

VIEW_COLUMN_CHOICES_ALL = set(SqlColumnDescription().__dict__.keys())

VIEW_COLUMN_CHOICES_DEFAULT = [
    'ordinal_position',
    'column_name',
    'column_type',
    'column_default',
    'is_nullable',
    'extra',
]