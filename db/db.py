import pymysql


def query_by_id(id):
    conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='888888',
                               db='material_info',
                               cursorclass=pymysql.cursors.DictCursor)
    print("Connection succeeds")
    cursor = conn.cursor()
    sql = "SELECT * FROM `material_info`.`material_info` " \
              "WHERE id = %s "
    cursor.execute(sql, [id])
    result = cursor.fetchall()
    return result[0]


def query_by_name(name):
    conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='888888',
                               db='material_info',
                               cursorclass=pymysql.cursors.DictCursor)
    print("Connection succeeds")
    cursor = conn.cursor()
    sql = "SELECT * FROM `material_info`.`material_info` " \
              "WHERE name = %s "
    cursor.execute(sql, [name])
    result = cursor.fetchall()
    return result


def query_by_category(category):
    conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='888888',
                               db='material_info',
                               cursorclass=pymysql.cursors.DictCursor)
    print("Connection succeeds")
    cursor = conn.cursor()
    sql = "SELECT * FROM `material_info`.`material_info` " \
              "WHERE category = %s "
    cursor.execute(sql, [category])
    result = cursor.fetchall()
    return result


def insert(id, name, category):
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='888888',
                               db='material_info',
                               cursorclass=pymysql.cursors.DictCursor)
        print("Connection succeeds")
        sql = "INSERT INTO `material_info`.`material_info` " \
              "(`id`, `name`, `category`) VALUES (%s, %s, %s)"
        cursor = conn.cursor()
        cursor.execute(sql, [id, name, category])
        conn.commit()
        print("Insertion succeeds")


# insert(888888, "sdd", "disk")
# print(query_by_id("8888"))
