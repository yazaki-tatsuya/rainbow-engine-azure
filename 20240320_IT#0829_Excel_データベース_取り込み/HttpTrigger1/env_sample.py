def get_env_variable(key):

    env_variable_dict = {
        # ------------------------------------
        # Azure Blob Storage
        # ------------------------------------
        "STORAGE_CONNECTION_STRING" : "接続文字列",
        "STORAGE_CONTAINER_NAME" : "コンテナー名",
        
        # ------------------------------------
        # SQL Server
        # ------------------------------------
        "SQL_SERVER_NAME" : "SQL Serverのサーバー名",
        "SQL_DATABASE_NAME" : "SQLデータベース名",
        "SQL_DATABASE_USER" : "SQLデータベースユーザー名",
        "SQL_DATABASE_PASS" : "SQLデータベースユーザーのPW"
    }
    ret_val = env_variable_dict.get(key, None)
    return ret_val