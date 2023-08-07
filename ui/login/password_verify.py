import bcrypt

# 用户注册或重置密码时调用此函数
def hash_password(password):
    # 生成随机的盐值并使用bcrypt哈希密码
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# 在用户注册或重置密码成功后，将哈希后的密码存储到数据库中
def save_hashed_password_to_database(username, hashed_password):
    pass
    # 将用户名和哈希后的密码存储到数据库中
    # 这里使用你的数据库插入操作代码

# 用户登录时调用此函数进行密码验证
def check_password(username, password):
    # 从数据库中获取该用户的哈希密码
    # 这里使用你的数据库查询操作代码
    # 哈希存储的密码从数据库中获取后是bytes类型，需要使用utf-8解码为字符串
    hashed_password_from_database = b'$2b$12$...'
    # 验证密码
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_database):
        print("密码正确，登录成功！")
        return True
    else:
        print("密码错误，登录失败！")
        return False