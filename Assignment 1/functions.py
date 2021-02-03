
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
    try:   
        sql = "SELECT * from keyword"
        cursor.execute(sql)
        rows = []
        if(keyword_id is not None):
            rows = cursor.fetchall();

        else: 
            for row in cursor.fetchall():
                if(row.keyword_id == keyword_id):
                    rows.append(row)
    
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
    try:   
        sql = "SELECT * from publication"
        cursor.execute(sql)
        rows = []
        if(member_id is not None):
            if(pub_type_id is not None):
                for(row in cursor.fetchall()):
                    
                

        else:

    except Exception as e:
        print(str(e))

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
    return
    

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
    return
