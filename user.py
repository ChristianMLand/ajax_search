from mysqlconnection import connectToMySQL
from server import DB

class User:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

    @classmethod
    def create(cls,data):
        query = '''
                INSERT INTO users
                (username)
                VALUES
                (%(username)s);
                '''
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM users;
                '''
        results = connectToMySQL(DB).query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users

    @staticmethod
    def filter(data):
        query = '''
                SELECT * FROM users
                WHERE username LIKE %(partial_username)s;
                '''
        return connectToMySQL(DB).query_db(query,data)