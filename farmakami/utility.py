import json

def dict_fetch_one(cursor):
    """
    Return one matching rows from a cursor as a dict
    """
    description = cursor.description
    row = cursor.fetchone()
    if row is not None:
        columns = [col[0] for col in description]
        return dict(zip(columns, row))
    return None


def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a list of dict
    """
    description = cursor.description
    rows = cursor.fetchall()
    if rows is not None:
        columns = [col[0] for col in description]
        return [
            dict(zip(columns, row))
            for row in rows
        ]
    return None

def count(cursor):
    """
    Return count from a cursor
    """
    return dict_fetch_one(cursor)['count']

class DatabaseAttributeError(object):
    def __init__(self, field_name, field_error):
        self.field_name = field_name
        self.field_error = field_error
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def __str__(self):
        return '<{}> Field Name : {}, Field Error : {}'.format(type(self).__name__, self.field_name, self.field_error)