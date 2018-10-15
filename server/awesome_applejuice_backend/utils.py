def data_missing(keys, body):
    return not all([key in body
                    for key in keys])


# TODO: organize 4xx error messages hierarchically.
def bad_request_missing_data(keys):
    quoted_keys = list(map(lambda x: f'"{x}"', keys))
    return f'Missing key among {", ".join(quoted_keys)}'
