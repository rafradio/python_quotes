import sys
import dbConnectSQL

def main(args):
    db = dbConnectSQL.DbConnectSQL()
    with open('users.txt', encoding="utf-8") as f:
        data = [line.rstrip() for line in f]
        
    print("Кол-во необходимых пользователей - ", len(data))
    db.checkSQLUsers(data)

if __name__ == "__main__":
    main(sys.argv)
    