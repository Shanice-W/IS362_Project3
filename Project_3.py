#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine

sql = '''SELECT
        c.LastName, c.FirstName, t.Name, a.Title
        FROM Customer as c
        JOIN Invoice as i
        ON c.CustomerId = i.CustomerId
        JOIN InvoiceLine as il
        ON i.InvoiceId = il.InvoiceId
        JOIN Track as t
        ON il.TrackId = t.TrackId
        JOIN Album as a
        ON t.AlbumID = a.AlbumId
        ORDER BY c.LastName, c.FirstName'''

db = create_engine('mysql+mysqlconnector://root:guitar@localhost:3306/Chinook')
pd.read_sql(sql, db).head(5)

