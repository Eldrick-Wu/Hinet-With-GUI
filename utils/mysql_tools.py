import mysql.connector
from mysql.connector import Error


class MySQLDatabase:
    def __init__(self, host, user, password, database):
        """初始化数据库连接"""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """建立与MySQL数据库的连接"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print(f"成功连接到数据库 {self.database}")
        except Error as e:
            print(f"无法连接到数据库: {e}")
            self.connection = None
            self.cursor = None

    def query_users(self, condition=None):
        """查询符合条件的users表内容"""
        try:
            if condition:
                query = f"SELECT * FROM users WHERE {condition}"
            else:
                query = "SELECT * FROM users"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if len(result) != 0:
                return result
            else:
                return None
        except Error as e:
            print(f"查询出错: {e}")
            return None

    def insert_user(self, user_data):
        """向users表插入一条数据"""
        try:
            query = "INSERT INTO users (user_name, user_password) VALUES (%s, %s)"
            self.cursor.execute(query, user_data)
            self.connection.commit()
            print("数据插入成功")
        except Error as e:
            print(f"插入数据出错: {e}")

    def delete_user(self, condition):
        """删除符合条件的用户"""
        try:
            query = f"DELETE FROM users WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print("数据删除成功")
        except Error as e:
            print(f"删除数据出错: {e}")

    def close(self):
        """关闭数据库连接"""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("数据库连接已关闭")


# 示例：如何使用这个类
if __name__ == "__main__":
    db = MySQLDatabase(host="localhost", user="root", password="884088haba", database="encrypt_users")

    # 查询用户
    users = db.query_users("username = 'john_doe'")
    print("查询结果:", users)

    # 插入新用户
    db.insert_user(('new_user', 'new_user@example.com', 'securepassword123'))

    # 删除用户
    db.delete_user("username = 'new_user'")

    # 关闭连接
    db.close()
