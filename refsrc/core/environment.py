class SingletonUser:
    _instances = dict()

    def __new__(cls, username, *args, **kwargs):
        if username not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[username] = instance
        return cls._instances[username]

    def __init__(self, username, data):
        self.username = username
        self.data = data

class UserPool:
    def __init__(self):
        self.pool = {}

    def get_user(self, username):
        if username not in self.pool:
            data = self.fetch_data_from_some_source(username)  # 这里是获取用户数据的逻辑
            user = SingletonUser(username, data)
            self.pool[username] = user
        return self.pool[username]

    def fetch_data_from_some_source(self, username):
        # 这里是获取用户数据的逻辑，比如从数据库或者API获取
        pass

"""
在这个例子中，SingletonUser类是一个单例类，它确保对于每一个用户名只创建一个对象。UserPool类是用户池，它用于获取用户的单例对象。如果用户对象还没有被创建，那么就创建一个新的对象并将其添加到用户池中。如果用户对象已经存在，那么就直接返回这个对象。
"""
