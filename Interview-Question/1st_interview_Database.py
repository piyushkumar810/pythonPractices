# -------------------------------------1st DataBase interview

# Q1) what is difference between DBMS and RDBMS
'''
ans ->              DBMS                                                    RDBMS
       -------------------------------------             --------------------------------------------
    -> DBMS is a software which is used to               where as RDBMS is a subset of DBMS where data is  
       interact with user,application and                stored in a form of tables (rows and columns).
       databasse itself to store, retrieve
       and manage data efficently.   
    -> stored in a form of herarchical, 
       network and file based structure. 

    -> data redundancy is high                            data redundancy is resolved by normalization
    -> acid property is not supported                     acid property is supported.
    -> multi-user access not supported                    multi-user acces is supported.
    -> eg:- xml, json                                     eg:- mysql, sqlite, oracle 
'''

# Q2) what do you mean by database and DBMS. types of DBMS?
'''
ans-> database is a collection of related data which stores data in a structured way so that you can read and access 
      data easily. 

      types of dbms:-
            hierarchial dbms-> here data is represented in the form of tree like structure.
            network dbms-> here data has many-to-many relationship
            relational dbms-> most used type of dbms because here data is expressed in the form of tables (row and column)
            object-oriented dbms-> here data is represented in the form of objects

'''

# Q3) advantages of dbms?
'''
ans-> Data Independence
      data security
      data recovery if data lost
      sharing of data
      redundancy control
'''

# Q4) mention the different languages present in the dbms?
'''
ans-> there are mainly 4 types of languges are:-

      Language	                           Purpose	                                     Key Commands
    ---------------                  ----------------                          ----------------------------  
    DDL (Data Definition)	         Defines database structure	                 CREATE, ALTER, DROP, TRUNCATE
    DML (Data Manipulation)	         Manipulates data	                         INSERT, UPDATE, DELETE, SELECT
    DCL (Data Control)	             Controls user permissions	                 GRANT, REVOKE
    TCL (Transaction Control)	     Manages transactions	                     COMMIT, ROLLBACK, SAVEPOINT
'''

# Q5) what do you understand by query optimization?
'''
ans-> query optimization is a technique of improving the efficiency of database query, the main goal is to 
       reduce execution time and resource consumption.

       example:- 
       Consider a table named Orders with 1 million records. Suppose you want to find all orders placed by 
       a specific customer (CustomerID = 101).

        1. Inefficient Query (Without Optimization)
            SELECT * FROM Orders WHERE CustomerID = 101;

            Problems:
            It scans the entire table (Orders), causing slow execution.
            If Orders has 1 million rows, it will check each row, consuming CPU and memory.

        2. Optimized Query (Using Indexing)
            CREATE INDEX idx_customer ON Orders(CustomerID);
            SELECT * FROM Orders WHERE CustomerID = 101;

            Why is this better?

            The index on CustomerID helps the database quickly locate relevant rows without scanning the entire table.
                Instead of checking all 1 million records, it directly fetches only the matching rows.
            Faster execution & lower resource usage (CPU, Disk I/O).

        3. Further Optimization (Selecting Only Required Columns)
            Instead of fetching all columns (SELECT *), selecting only the necessary columns improves performance:

            SELECT OrderID, OrderDate FROM Orders WHERE CustomerID = 101;

            Benefits:
            Reduces data transfer time (especially in large tables).
            Improves query performance by retrieving only relevant information.
'''