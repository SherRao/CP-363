"""
------------------------------------------------------------------------
Assignment #4
------------------------------------------------------------------------
Author:  Nausher Rao
ID:      190906250
Email:   raox6250@mylaurier.ca
Section: CP363 Winter 2021
__updated__ = "2021-03-16"
------------------------------------------------------------------------
"""

def get_table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = get_table_info(cursor, table_schema)
    Use: rows = get_table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields data)
            if table_name is not None:
                rows containing table_name
            else:
                all TABLES rows
            Sorted by TABLE_NAME, TABLE_TYPE
    -------------------------------------------------------
    """
    sql = """
    SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT 
    FROM information_schema.TABLES 
    WHERE TABLE_SCHEMA = %s 
    """;
    
    params = [table_schema];
    if(table_name is not None):
        sql += """AND TABLE_NAME = %s """
        params.append(table_name);

    sql += """ORDER BY TABLE_NAME, TABLE_TYPE;""";
    cursor.execute(sql, params);
    return cursor.fetchall();



def get_column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = get_column_info(cursor, table_schema)
    Use: rows = get_column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields data)
            if table_name is not None:
                rows containing table_name
            else:
                all COLUMNS rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    sql = """
    SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
    FROM information_schema.COLUMNS 
    WHERE TABLE_SCHEMA = %s 
    """;

    params = [table_schema];
    if(table_name is not None):
        sql += """AND TABLE_NAME = %s """
        params.append(table_name);

    sql += """ORDER BY TABLE_NAME, COLUMN_NAME;""";
    cursor.execute(sql, params);
    return cursor.fetchall();



def get_constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = get_constraint_info(cursor, table_schema)
    Use: rows = get_constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields data)
            if constraint_type is not None:
                rows containing constraint_type
            else:
                all TABLE_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME
    -------------------------------------------------------
    """
    sql = """
    SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE  
    FROM information_schema.TABLE_CONSTRAINTS 
    WHERE TABLE_SCHEMA = %s 
    """;

    params = [table_schema];
    if(constraint_type is not None):
        sql += """AND CONSTRAINT_TYPE = %s """
        params.append(constraint_type);

    sql += """ORDER BY CONSTRAINT_NAME, TABLE_NAME;""";
    cursor.execute(sql, params);
    return cursor.fetchall();



def get_foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = get_foreign_key_info(cursor, constraint_schema)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields data)
            if table_name and/or ref_table_name are not None:
                rows containing table_name and/or ref_table_name
            else:
                all REFERENTIAL_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
    -------------------------------------------------------
    """
    sql = """
    SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, TABLE_NAME, REFERENCED_TABLE_NAME 
    FROM information_schema.REFERENTIAL_CONSTRAINTS 
    WHERE CONSTRAINT_SCHEMA = %s 
    """;

    params = [constraint_schema];
    if(table_name is not None):
        sql += """AND TABLE_NAME = %s """
        params.append(table_name);

        if(ref_table_name is not None):
            sql += """AND REFERENCED_TABLE_NAME = %s """
            params.append(ref_table_name);    

    elif(ref_table_name is not None):
            sql += """AND REFERENCED_TABLE_NAME = %s """
            params.append(ref_table_name);

    sql += """ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME;""";
    cursor.execute(sql, params);
    return cursor.fetchall();



def get_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = get_key_info(cursor, constraint_schema)
    Use: rows = get_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = get_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = get_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields data)
            if table_name and/or ref_table_name are not None:
                rows containing table_name and/or ref_table_name
            else:
                all KEY_COLUMN_USAGE rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    sql = """
    SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME 
    FROM information_schema.KEY_COLUMN_USAGE 
    WHERE CONSTRAINT_SCHEMA = %s 
    """;

    params = [constraint_schema];
    if(table_name is not None):
        sql += """AND TABLE_NAME = %s """
        params.append(table_name);

        if(ref_table_name is not None):
            sql += """AND REFERENCED_TABLE_NAME = %s """
            params.append(ref_table_name);    

    elif(ref_table_name is not None):
            sql += """AND REFERENCED_TABLE_NAME = %s """
            params.append(ref_table_name);

    sql += """ORDER BY TABLE_NAME, COLUMN_NAME;""";
    cursor.execute(sql, params);
    return cursor.fetchall();