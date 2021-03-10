def get_all_pub_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the numbers of publications of each type data.
            Name these three fields "articles", "papers", and "books")
            if member_id is not None:
                rows containing member_id
            else:
                all member and publication rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, 
     (SELECT COUNT(Publication.pub_type_id) FROM pub AS Publication WHERE Publication.pub_type_id = 'a' AND Member.member_id = Publication.member_id) AS articles,
     (SELECT COUNT(Publication.pub_type_id) FROM pub AS Publication WHERE Publication.pub_type_id = 'p' AND Member.member_id = Publication.member_id) AS papers,
     (SELECT COUNT(Publication.pub_type_id) FROM pub AS Publication WHERE Publication.pub_type_id = 'b' AND Member.member_id = Publication.member_id) AS books
     FROM member AS Member
    """;
    data = [];
    if(member_id is not None):
        sql += " WHERE Member.member_id = %s";
        data.append(member_id);

    sql += """
     ORDER BY Member.last_name, Member.first_name;
     """;
    cursor.execute(sql, data);
    #rows = cursor.fetchall();
    #for i in range(len(row)):
    #    rows[i] = rows[i][]
    
    return cursor.fetchall();


def get_expertise_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_expertise_counts(cursor)
    Use: rows = get_expertise_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of keywords and supplementary keywords
            for the member data. Name these fields "keywords" and "supp_keys")
            if member_id is not None:
                rows containing member_id
            else:
                all member, keyword, and supplementary keyword rows
            Sorted by last name, first name
   -------------------------------------------------------
    """
    sql = """
    SELECT Member.last_name, Member.first_name, 
     (SELECT COUNT(MemberKeyword.keyword_id) FROM member_keyword AS MemberKeyword WHERE Member.member_id = MemberKeyword.member_id) AS keywords,
     (SELECT COUNT(SupplementaryKeyword.supp_key_id) FROM member_supp_key AS SupplementaryKeyword WHERE Member.member_id = SupplementaryKeyword.member_id) AS supp_keys
     FROM member AS Member
    """;
    data = [];
    if(member_id is not None):
        sql += " WHERE Member.member_id = %s";
        data.append(member_id);

    sql += """
     ORDER BY Member.last_name, Member.first_name;
     """;
    cursor.execute(sql, data);
    return cursor.fetchall();


def get_keyword_counts(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_keyword_counts(cursor)
    Use: rows = get_keyword_counts(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of a keyword's description and the number of
            supplementary keywords that belong to it data. Name the
            second field "supp_key_count".)
            if keyword_id is not None:
                rows containing keyword_id
            else:
                all keyword and supplementary keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    sql = """
    SELECT Keyword.k_desc, 
     (SELECT COUNT(SupplementaryKeyword.supp_key_id) FROM supp_key AS SupplementaryKeyword WHERE Keyword.keyword_id = SupplementaryKeyword.keyword_id) AS supp_key_count
     FROM keyword AS Keyword
    """;
    data = [];
    if(keyword_id is not None):
        sql += " WHERE Keyword.keyword_id = %s";
        data.append(keyword_id);

    sql += """
     ORDER BY Keyword.k_desc;
     """;
    cursor.execute(sql, data);
    return cursor.fetchall();


def get_keyword_member_counts(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_keyword_member_counts(cursor)
    Use: rows = get_keyword_member_counts(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of a keyword description and the number of members
            that have it data. Name the second field "member_count".)
            if keyword_id is not None:
                rows containing keyword_id
            else:
                all member and keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    sql = """
    SELECT Keyword.k_desc, 
     (SELECT COUNT(MemberKeyword.member_id) FROM member_keyword AS MemberKeyword WHERE MemberKeyword.keyword_id = Keyword.keyword_id) AS member_count
     FROM keyword AS Keyword
    """;
    data = [];
    if(keyword_id is not None):
        sql += " WHERE Keyword.keyword_id = %s";
        data.append(keyword_id);

    sql += """
     ORDER BY Keyword.k_desc, member_count;
     """;
    cursor.execute(sql, data);
    return cursor.fetchall();


def get_supp_key_member_counts(cursor, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_supp_key_member_counts(cursor)
    Use: rows = get_supp_key_member_counts(cursor, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - (list of a keyword's description, a supplementary
            keyword description, and the number of members that have that
            supplementary expertise data. Name the last field "member_count".)
            if supp_key_id is not None:
                rows containing supp_key_id
            else:
                all member, keyword, and supplementary keyword rows
            Sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """
    sql = """
    SELECT keyword.k_desc, supp_key.sk_desc, 
     (SELECT COUNT(member_supp_key.member_id) FROM member_supp_key WHERE member_supp_key.supp_key_id = supp_key.supp_key_id) AS member_count
     FROM keyword, supp_key
     WHERE keyword.keyword_id = supp_key.keyword_id
    """;
    data = [];
    if(supp_key_id is not None):
        sql += " AND supp_key_id = %s";
        data.append(supp_key_id);

    sql += """
     GROUP BY keyword.k_desc, supp_key.sk_desc, member_count
     ORDER BY keyword.k_desc, supp_key.sk_desc;
     """;
    cursor.execute(sql, data);
    return cursor.fetchall();