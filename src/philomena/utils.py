

def form_query(params: dict) -> str:
    query_params = '?'
    for key, value in params.items():
        query_params = f'{query_params}&{key}={value}'
    if query_params:
        return query_params
