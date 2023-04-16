# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:14:10 2022

@author: watson
"""
作業：

請使用 python 程式來執行SQL 相關東西

請建立一個資料庫：jobs
create database jobs;
use jobs

在這個資料庫中建立二個資料表

employee    id ,name,sex,tel,assume(日期)
create table employee(
	     -> id int primary key auto_increment,
	     -> name varchar(20),
	     -> sex varchar(2),
         -> tel varchar(12),
         -> assume date);

works  id,items,info,employeeid
create table works(
        -> id int primary key auto_increment,
        -> items varchar(20),
        -> info text,
        ->employeeid int);

由python 程式撰寫：
mylccdb.py 設定db
main.py 解以下的要求

使用者依輸入的方式填入：員工姓名、性別、電話 ，程式新增到 employee 的資料表中

使用者依輸入的方式填入：工作項目、工作詳述、對應的員工編號(id)

使用者可以依員工id 來修改員工的電話及性別

使用者可以依員工編號來查詢員工的基本資料

使用者輸入員工編號，請印出員工姓名及工作項目、工作詳述











