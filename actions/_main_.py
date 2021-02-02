# coding=utf-8
from MySQLdb import _mysql


def main(dict):
    company = dict["company"]
    name = dict["name"]
    telephone = dict["telephone"]
    email = dict["email"]
    detail = dict["detail"]
    if telephone is None or email is None:
        return {"Error Code": "404 contact method not found"}
    else:
        command = "insert into consulting_info (company,name,telephone,email,detail) " \
                  "values ('%s','%s','%s','%s','%s')" % (company, name, telephone, email, detail)
        # result = mysql_command_execute(command)

        return {"result": command}


def mysql_command_execute(command):
    db = _mysql.connect(
        host='rm-p0wodj1r55acz1932lo.mysql.australia.rds.aliyuncs.com',
        user='lyz_leo',
        passwd='sysAdmin1',
        db='test_db',
    )
    db.query(command)
    r = db.store_result()
    if r is not None:
        return r.fetch_row(maxrows=0, how=1)
    else:
        return {"Response Code": "1 succeed!"}

