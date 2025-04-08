from api.config import dbConnection
import json

def get_all_movies(params):
    query = "SELECT * FROM movies"
    
    where_clauses = []
    query_params = []

    # Handling kompleks untuk filter genre (array)
    if 'genre' in params:
        where_clauses.append("genre::text LIKE %s")
        query_params.append(f"%{params['genre']}%")

    # Handling filter durasi
    if 'duration' in params:
        # Misalnya filter durasi minimal
        where_clauses.append("duration::numeric >= %s")
        query_params.append(float(params['duration']))

    # Handling filter user rating
    if 'user_rating' in params:
        where_clauses.append("(user_rating)::numeric >= %s")
        query_params.append(float(params['user_rating']))

    # Handling filter name (pencarian parsial)
    if 'name' in params:
        where_clauses.append("name::text ILIKE %s")
        query_params.append(f"%{params['name']}%")

    # Handling filter id
    if 'id' in params:
        where_clauses.append("id = %s")
        query_params.append(int(params['id']))

    # Tambahkan WHERE clause jika ada filter
    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)

    # Sorting
    sort_by = params.get('sort_by', 'id')
    sort_order = params.get('sort_order', 'ASC')
    
    # Daftar field yang diizinkan untuk sorting
    allowed_sort_fields = ['id', 'name', 'genre', 'duration', 'user_rating']
    sort_by = sort_by if sort_by in allowed_sort_fields else 'id'
    sort_order = sort_order.upper() if sort_order.upper() in ['ASC', 'DESC'] else 'ASC'
    
    query += f" ORDER BY {sort_by} {sort_order}"

    # Pagination
    page = int(params.get('page', 1))
    size = int(params.get('size', 10))
    offset = (page - 1) * size

    query += " LIMIT %s OFFSET %s"
    query_params.extend([size, offset])

    return dbConnection.command_with_params(query, query_params)