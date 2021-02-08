from Connect import Connect;

def get_keywords(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the keyword table.
    Use: rows = get_keywords(cursor)
    Use: rows = get_keywords(cursor, keyword_id=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID (int)
    Returns:
        rows - (list of keyword table data)
            if keyword_id is not None:
                rows matching keyword_id
            else:
                the entire keyword table
            Sorted by keyword description
    -------------------------------------------------------
    """
    rows = []
    try:   
        sql = "SELECT * from keyword"
        if(keyword_id is not None):
            sql += " WHERE keyword_id = %s"

        sql += " ORDER BY k_desc"

        data = []
        if(keyword_id is not None):
            data.append(keyword_id)

        cursor.execute(sql, data)
        rows = cursor.fetchall()
    
    except Exception as e:
        print(str(e))

    return rows


def get_publications(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = get_publications(cursor)
    Use: rows = get_publications(cursor, member_id=v1)
    Use: rows = get_publications(cursor, pub_type_id=v2)
    Use: rows = get_publications(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - (list of pub table data)
            if member_id and/or pub_type_id are not None:
                rows matching member_id and/or pub_type_id
            else:
                the entire pub table
            Sorted by publication title
    -------------------------------------------------------
    """
    rows = []
    sql = "SELECT * from pub"
    if(member_id is not None):
        sql += " WHERE member_id = %s"
        if(pub_type_id is not None):
            sql += " AND pub_type_id = %s"

    elif(pub_type_id is not None):
        sql += " WHERE pub_type_id = %s"

    sql += " ORDER BY p_title"
    data = []
    if(member_id is not None):
        data.append(member_id)

    if(pub_type_id is not None):
        data.append(pub_type_id)

    cursor.execute(sql, data)
    rows = cursor.fetchall()
    return rows


def get_member_expertises(cursor, member_id=None, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = get_member_expertises(cursor)
    Use: rows = get_member_expertises(cursor, member_id=v1)
    Use: rows = get_member_expertises(cursor, keyword_id=v2)
    Use: rows = get_member_expertises(cursor, member_id=v1, keyword_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of v_member_keyword view data)
            if member_id and/or keyword_id are not None:
                rows matching member_id and/or keyword_id
            else:
                the entire v_member_keyword view
            Sorted by member last name, first name, and keyword description
    -------------------------------------------------------
    """
    rows = []
    try:   
        sql = "SELECT * from v_member_keyword"
        if(member_id is not None):
            sql += " WHERE member_id = %s"
            if(keyword_id is not None):
                sql += " AND keyword_id = %s"

        elif(keyword_id is not None):
            sql += " WHERE keyword_id = %s"

        sql += " ORDER BY last_name, first_name, k_desc"

        data = []
        if(member_id is not None):
            data.append(member_id)

        if(keyword_id is not None):
            data.append(keyword_id)

        cursor.execute(sql, data)
        rows = cursor.fetchall()
    
    except Exception as e:
        print(str(e))

    return rows
    

def get_expertises(cursor, keyword=None, supp_key=None):
    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = get_expertises(cursor)
    Use: rows = get_expertises(cursor, keyword=v1)
    Use: rows = get_expertises(cursor, supp_key=v2)
    Use: rows = get_expertises(cursor, keyword=v1, supp_key=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword - a partial keyword description (str)
        supp_key - a partial supplementary description (str)
    Returns:
        rows - (list of v_keyword_supp_key view data)
            if keyword and/or supp_key are not None:
                rows containing keyword and/or supp_key
            else:
                the entire v_keyword_supp_key view
            Sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """
    rows = []
    try:   
        sql = "SELECT * from v_keyword_supp_key"
        if(keyword is not None):
            sql += " WHERE keyword_id = %s"
            if(supp_key is not None):
                sql += " AND supp_key_id = %s"

        elif(supp_key is not None):
            sql += " WHERE supp_key_id = %s"

        sql += " ORDER BY k_desc, sk_desc"

        data = []
        if(keyword is not None):
            data.append(keyword)

        if(supp_key is not None):
            data.append(supp_key)

        cursor.execute(sql, data)
        rows = cursor.fetchall()
    
    except Exception as e:
        print(str(e))

    return rows