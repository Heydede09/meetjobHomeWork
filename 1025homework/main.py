# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 07:26:12 2022

@author: User
"""

import mylccdb
from datetime import datetime

def addEmployee(name,sex,tel):
    now = datetime.now()
    today = datetime.strftime(now,'%Y-%M-%d')
    sql = "insert into employee(name,sex,tel,assume) values ('{}','{}','{}','{}')".format(name,sex,tel,today)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    
    
def addWorks(employeeid,items,info):
    sql = "insert into wroks(items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    
def allEmployee():
    sql = "select id,name from employee"
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    result = cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名：",row[1])
        print()
        
def queryEmplyee(employeeid):
    
    sql = "select id,name,sex,assume,tel from employee where id ='{}'".format(employeeid)
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    result = cursor.fetchall()
    for row in result:
        print("員工編號:",row[0])
        print("員工姓名：",row[1])
        print("員工性別：",row[2])
        print("就職日：",row[3])
        print("電話：",row[4])
        print()
    else:
        print("沒有這個員工")
        
def updateEmplyee(employeeid,tel,sex):
    sql = "update employee set tel='{}',sex='{}' where id='{}'".format(tel,sex,employeeid)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    
def queryEmplyeeWorks(employeeid):
    sql = "select employee.name,wroks.* from employee inner join wroks on employee.id = wrokse.employeeid where employee.id = '{}'".format(employeeid)
    
    cursor = mylccdb.conn.cursor()
    cursor.execute(sql)
    mylccdb.conn.commit()
    
    result = cursor.fetchall()
    
    for row in result:
        print("員工：",row[0])
        print("工作項目：",row[2])
        print("工作內容：",row[3])
        print()
        
if __name__== "__main__":
    while True:
        item = input("員工系統：a->新增員工 w->新增員工工作 q->查詢 u-> 修改 e->員工的工作內容 x->離開:")
    
        if item =="x":
            break
        elif item == "a":
            name = input("新員工姓名：")
            sex = input("性別(F/M):")
            tel = input("電話：")
            addEmployee(name,sex,tel) #新增
            allEmployee() #顯示所有員工
        elif item == "w":
            allEmployee() #顯示所有員工
        
            empId = input("請輸入員工編號：")
            item = input("請輸入工作事項：")
            info = input("請輸入內容：")
            addWorks(empId,item,info)
        elif item == "q":
            eid = input("請輸入員工編號：")
            queryEmplyee(eid)
            
        elif item =="u":
            allEmployee() #顯示所有員工
            
            eid = input("請輸入員工編號：")
            tel = input("請輸入修改的電話：")
            sex = input("請輸入修改的性別(F/M):")
            updateEmplyee(eid,tel,sex)
        elif item == "e":
            employeeid= input ("請輸入員工編號：")
            queryEmplyeeWorks(employeeid)
            
            
            
            
    