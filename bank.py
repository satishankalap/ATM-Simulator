import random
from parsing import GetDict
import mysql.connector
cred=GetDict()
conn=mysql.connector.connect(**cred)
cur=conn.cursor()

#Creating a 16 digit random password.

def pin():
    l1=[i for i in range(10)]
    l2=[chr(i) for i in range(97,122)]
    code="MB"
    a=random.sample(l1,3)
    b=random.sample(l2,4)
    c=random.sample(l1,4)
    d=random.sample(l2,3)
    e=a+b+c+d
    new=""
    for i in e:
        new=new+str(i)
    return code+new
pin()

#Creating a account number.

def randomNumber():
    num=[nums for nums in range(10)]
    random_gen=random.sample(num,8)
    random_acc=""
    for n in random_gen:
        random_acc=random_acc+str(n)
    return random_acc

def accountNumber():
    number=randomNumber()
    checkid="SELECT * FROM details"
    cur.execute(checkid)
    gen_id=cur.fetchall()
    acc_num=str(len(gen_id))+number
    return acc_num
accountNumber()
