from flask_app.config.mysqlconnection import connectToMySQL

class User:


    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """
        result = connectToMySQL('users').query_db(query = query)
        users = []
        for item in result:
            users.append(cls(item))
        return users
    
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM users WHERE id = %(id)s;
        """
        result = connectToMySQL('users').query_db(query,data)
        if result:
            result = cls(result[0])
        return result
    
    @classmethod
    def update_user(cls, data):
        query = """
            UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s WHERE id = %(id)s ;
        """
        result = connectToMySQL("users").query_db(query , data)
        print("*"*30,result)
        return result
    
    @classmethod
    def delete_user(cls , data):
        query = """
            DELETE FROM users WHERE id = %(id)s ;
        """
        result = connectToMySQL("users").query_db(query , data)
        return result
