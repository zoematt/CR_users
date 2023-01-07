from mysqlconnection import connectToMySQL

db='users_schema' 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data ['email']
        self.created_at = data["created_at"]
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
        INSERT into users (first_name, last_name, email) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def getall_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(db).query_db(query)
        
        users = []
        for user in results:
            users.append(cls(user))

        return connectToMySQL(db).query_db(query)