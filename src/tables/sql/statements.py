from __future__ import annotations
from tables.domain.enums import SqlTableType

GET_ALL_DATABASE_TABLES = f'''
    SELECT 
        info.TABLE_NAME AS table_name,
        info.TABLE_TYPE AS table_type
    FROM 
        information_schema.tables info
    WHERE 
        table_type IN ('{SqlTableType.TABLE.value}', '{SqlTableType.VIEW.value}')
        AND TABLE_SCHEMA = %s
    ORDER BY 
        table_name;
'''