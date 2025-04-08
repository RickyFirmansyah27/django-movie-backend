from api.config import dbConnection
import json

def get_all_movies(params):
    query = "SELECT * FROM movies"
    query_count = "SELECT COUNT(*) FROM movies"
    
    where_clauses = []
    query_params = []

    if 'genre' in params:
        where_clauses.append("genre::text LIKE %s")
        query_params.append(f"%{params['genre']}%")

    if 'duration' in params:

        where_clauses.append("duration::numeric >= %s")
        query_params.append(float(params['duration']))

    if 'user_rating' in params:
        where_clauses.append("(user_rating)::numeric >= %s")
        query_params.append(float(params['user_rating']))

    if 'name' in params:
        where_clauses.append("name::text ILIKE %s")
        query_params.append(f"%{params['name']}%")

    if 'id' in params:
        where_clauses.append("id = %s")
        query_params.append(int(params['id']))

    if where_clauses:
        query += " WHERE " + " AND ".join(where_clauses)

    sort_by = params.get('sort_by', 'id')
    sort_order = params.get('sort_order', 'ASC')
    
    allowed_sort_fields = ['id', 'name', 'genre', 'duration', 'user_rating']
    sort_by = sort_by if sort_by in allowed_sort_fields else 'id'
    sort_order = sort_order.upper() if sort_order.upper() in ['ASC', 'DESC'] else 'ASC'
    
    query += f" ORDER BY {sort_by} {sort_order}"

    page = int(params.get('page', 1))
    size = int(params.get('size', 5))
    offset = (page - 1) * size

    query += " LIMIT %s OFFSET %s"
    query_params.extend([size, offset])
    total_data = dbConnection.command_with_params(query_count, query_params)[0][0]
    data = dbConnection.command_with_params(query, query_params)

    return total_data, data