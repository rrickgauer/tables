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



GET_TABLE_COLUMNS_INFO = '''
    SELECT 
        info.ORDINAL_POSITION         AS ordinal_position,
        info.COLUMN_NAME              AS column_name,
        info.COLUMN_DEFAULT           AS column_default,
        info.IS_NULLABLE              AS is_nullable,
        info.DATA_TYPE                AS data_type,
        info.CHARACTER_MAXIMUM_LENGTH AS character_maximum_length,
        info.CHARACTER_OCTET_LENGTH   AS character_octet_length,
        info.NUMERIC_PRECISION        AS numeric_precision,
        info.NUMERIC_SCALE            AS numeric_scale,
        info.DATETIME_PRECISION       AS datetime_precision,
        info.CHARACTER_SET_NAME       AS character_set_name,
        info.COLLATION_NAME           AS collation_name,
        info.COLUMN_TYPE              AS column_type,
        info.COLUMN_KEY               AS column_key,
        info.EXTRA                    AS extra,
        info.PRIVILEGES               AS privileges,
        info.COLUMN_COMMENT           AS column_comment,
        info.GENERATION_EXPRESSION    AS generation_expression,
        info.SRS_ID                   AS srs_id
    FROM 
        information_schema.COLUMNS info
    WHERE 
        TABLE_SCHEMA = %s 
        AND TABLE_NAME = %s
    Order BY
        ordinal_position ASC;
'''