from parsing import GetDict
import mysql.connector
from bank import pin,accountNumber
from date import Date
from statement import Statement


Date=Date()

options=int(input("\t\t\t WELCOME TO MYBANK\n\t\t\t 1.Create Account\n\t\t\t 2.Existing Customer\n"))

# Database connections Modify According to Developer Data
cred=GetDict()
conn=mysql.connector.connect(**cred)
cur=conn.cursor()


auto_pin=pin()
accountNumber=accountNumber()
statement=Statement()




try:
    #Creating Account
    def createAccount():
        if options==1:
            accounttype=int(input("\t\t\t 1.Current Account \n\t\t\t 2.Savings Account\n"))
            #Current Account
            if accounttype==1:
                print(Date)
                name=input("Enter Your Name:")
                email=input("Enter Your Email:")
                mobile=input("Enter Your Mobile-Number:")
                amount=int(input("Enter Amount:"))
                account="Current"
                accountnum=accountNumber
                if amount>=500:
                    otp=auto_pin
                    # Create a table and insert into that particular table
                    add="INSERT INTO details(name,email,mobile,amount,acc_type,password,acc_number) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    info=(name,email,mobile,amount,account,otp,accountnum)
                    cur.execute(add,info)
                    conn.commit()
                    print("Thanks for creating your account in MYBANK your account number is "+accountnum+" and your password is "+otp)
                else:
                    print("Minimum Amount 500 To Create Account")
                                
            #Savings Account   
            elif accounttype==2:
                
                name=input("Enter Your Name:")
                email=input("Enter Your Email:")
                mobile=input("Enter Your Mobile-Number:")
                amount=int(input("Enter Amount:"))
                account="Savings"
                #Automatic Generation of Account Number
                accountnum=accountNumber
                if amount>=500:
                    #Automatic Generation of Password
                    otp=auto_pin
                    add="INSERT INTO details(name,email,mobile,amount,acc_type,password,acc_number) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    info=(name,email,mobile,amount,account,otp,accountnum)
                    cur.execute(add,info)
                    conn.commit()
                    print("Thanks for creating your account in MYBANK your account number is "+accountnum+" and your password is "+otp)

                else:
                    print("Minimum Amount 500 To Create Account")

    createAccount()  
    # Function for validating the password     
    def checkCredentials(password):
        check="SELECT name FROM details WHERE password=%s"
        value=(password,)
        cur.execute(check,value)
        res=cur.fetchall()
        if len(res)==1:
            for i in res:
                for name in i:
                    print("Welcome "+name)
            return 1
        else:
            return 0
            
    #Validating existing customer
    def existingCustomer():
        if options==2:
            acc_num=input("Enter Your Account Number:")
            password=input("Enter Your Password:")
            op=checkCredentials(password)
            if op==1:
                index=int(input("\t\t\t 1.Account Statement \n\t\t\t 2.Withdraw \n\t\t\t 3.Deposit \n\t\t\t 4.Change Password \n"))
                #Account Statement
                if index==1:
                    statement(acc_num)
                #Withdraw
                elif index==2:
                    print(Date)
                    debit=int(input("Enter Amount:"))
                    def Withdraw():
                        check="SELECT amount FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        available=""
                        for amount in res:
                            available=available+amount[0]
                        if debit>int(available):
                            print("Insufficient Amount")
                        else:
                            remaining=int(available)-debit
                            update = "UPDATE details SET amount =%s WHERE acc_number =%s"
                            val=(remaining,acc_num)
                            cur.execute(update,val)
                            conn.commit()
                            print("Please collect your cash")
                            print("Available Balance "+str(remaining))                    
                    Withdraw()
                #Deposit
                elif index==3:
                    print(Date)
                    credit=int(input("Enter Amount:"))
                    def Deposit():
                        check="SELECT amount FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        available=""
                        for amount in res:
                            available=available+amount[0]
                        total_amount=int(available)+credit
                        update = "UPDATE details SET amount =%s WHERE acc_number =%s"
                        val=(total_amount,acc_num)
                        cur.execute(update,val)
                        conn.commit()
                        print("Deposited Successfully")
                        print("Available Balance "+str(total_amount))
                    Deposit()
                #For modifying password
                elif index==4:
                    def modify_password():
                        check="SELECT password FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        current_password=""
                        for password in res:
                            current_password=current_password+password[0]
                        new_password=input("Enter New Password:")
                        update = "UPDATE details SET password =%s WHERE password =%s"
                        val=(new_password,current_password)
                        cur.execute(update,val)
                        conn.commit()
                        print("Password Changed Successfully")
                        print("Your New Password is "+new_password)
                    modify_password()  
            else:
                print("Incorrect Password")
    existingCustomer()
except Exception as e:
    print(e)
