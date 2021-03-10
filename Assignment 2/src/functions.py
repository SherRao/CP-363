def get_member_publications(cursor, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_member_publications(cursor)
    Use: rows = get_member_publications(cursor, title=v1)
    Use: rows = get_member_publications(cursor, pub_type_id=v2)
    Use: rows = get_member_publications(cursor, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        title - a partial title (str)
        pub_type_id - a publication type (str)

    Returns:
        rows - (list of member's last name, a member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a') data)
            if title and/or pub_type_id are not None:
                rows containing title and/or pub_type_id
            else:
                all member and publication rows
            Sorted by last name, first name, title
    -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, Publication.p_title, PublicationType.pt_desc
     FROM pub AS Publication
     INNER JOIN member AS Member ON Member.member_id = Publication.member_id
     INNER JOIN pub_type AS PublicationType ON PublicationType.pub_type_id = Publication.pub_type_id
    """
    
    data = []
    if(title is not None):
        sql += " WHERE Publication.p_title LIKE %s"
        data.append("%" + title + "%")
        if(pub_type_id is not None):
            sql += " AND Publication.pub_type_id = %s"
            data.append(pub_type_id)

    elif(pub_type_id is not None):
        sql += " WHERE Publication.pub_type_id = %s"
        data.append(pub_type_id)

    sql += " ORDER BY Member.last_name, Member.first_name, Member.title;"
    cursor.execute(sql, data)
    return cursor.fetchall()   


def get_publication_counts(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_publication_counts(cursor)
    Use: rows = get_publication_counts(cursor, member_id=v1)
    Use: rows = get_publication_counts(cursor, pub_type_id=v2)
    Use: rows = get_publication_counts(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of publications of type
            pub_type_id data)
            if member_id or pub_type_id is not None:
                rows containing member_id and/or pub_type_id
            else:
                all member names and publication counts
            Sorted by last name, first name
    -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, COUNT(Publication.pub_type_id)
     FROM pub AS Publication
     INNER JOIN member AS Member ON Publication.member_id = Member.member_id
    """
    
    data = []
    if(member_id is not None):
        sql += " WHERE Member.member_id = %s"
        data.append(member_id)
        if(pub_type_id is not None):
            sql += " AND Publication.pub_type_id = %s"
            data.append(pub_type_id)

    elif(pub_type_id is not None):
        sql += " WHERE Publication.pub_type_id = %s"
        data.append(pub_type_id)

    sql += """
     GROUP BY Publication.member_id
     ORDER BY Member.last_name, Member.first_name;
    """

    cursor.execute(sql, data)
    return cursor.fetchall()


def get_keyword_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member and keyword tables.
    Use: rows = get_keyword_counts(cursor)
    Use: rows = get_keyword_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of expertises (i.e. keywords)
            they hold data)
            if member_id is not None:
                rows containing member_id
            else:
                all member and expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, COUNT(Keyword.k_desc)
     FROM member AS Member
     INNER JOIN member_keyword AS MemberKeyword ON MemberKeyword.member_id = Member.member_id
     INNER JOIN keyword AS Keyword ON MemberKeyword.keyword_id = Keyword.keyword_id
    """
    
    data = []
    if(member_id is not None):
        sql += " WHERE Member.member_id = %s"
        data.append(member_id)

    sql += """
     GROUP BY Member.last_name, Member.first_name
     ORDER BY Member.last_name, Member.first_name
    """
    
    cursor.execute(sql, data)
    return cursor.fetchall()



def get_all_expertises(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member, keyword, and supp_key tables
    Use: rows = get_all_expertises(cursor)
    Use: rows = get_all_expertises(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, a keyword description, and a supplementary
            keyword description data)
            if member_id is not None:
                rows containing member_id
            else:
                all member and expertise rows
            Sorted by last name, first name, keyword description, supplementary
                keyword description
    -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, Keyword.k_desc, SupplementaryKeyword.sk_desc
    FROM member AS Member
    INNER JOIN member_keyword AS MemberKeyword ON Member.member_id = MemberKeyword.member_id
    INNER JOIN keyword AS Keyword ON Keyword.keyword_id = MemberKeyword.keyword_id
    INNER JOIN supp_key AS SupplementaryKeyword ON SupplementaryKeyword.keyword_id = MemberKeyword.keyword_id
    """
    data = []
    if(member_id is not None):
        sql += " WHERE Member.member_id = %s"
        data = [member_id]

    sql += """ 
     GROUP BY Member.last_name, Member.first_name, Keyword.k_desc, SupplementaryKeyword.sk_desc
     ORDER BY Member.last_name, Member.first_name, Keyword.k_desc, SupplementaryKeyword.sk_desc;
    """

    cursor.execute(sql, data)
    return cursor.fetchall()