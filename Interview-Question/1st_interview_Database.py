# -------------------------------------1st DataBase interview

# Q1) what is difference between DBMS and RDBMS
'''
ans ->              DBMS                                                    RDBMS
       -------------------------------------             --------------------------------------------
    -> DBMS is a software which is used to               where as RDBMS is a subset of DBMS where data is  
       interact with user, application and               stored in a form of tables (rows and columns).
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

# Q6) do we consider NUll value same as that of blank space or zero?
'''
ans-> No null value is not at all same as blank space or zero. here are the difference

        Value	                   Meaning	                                      Example
    ---------------           ---------------------------                ------------------------------    
     NULL	                   Unknown / Missing value	           NULL in SQL means no value has been assigned.
     Blank Space (' ')	     A valid but empty string	           ' ' (a space) is considered as a string with no characters.
     Zero (0)	               A numerical value	               0 is an actual number and is not NULL.
'''

# Q7) what do you understand by aggregation and atomicity?
'''
ans-> 1. Aggregation
            Aggregation is a feature in Entity-Relationship (ER) models where a relationship between 
            two entities is treated as a higher-level entity.

            It is used when we need to relate a relationship with another entity.
            It helps in modeling complex relationships in databases.

            example:- A Teacher teaches a Course.
                      A Student enrolls in a Course.

    2. Atomicity (A in ACID Properties)
            Atomicity ensures that a database transaction is treated as a single unit that either 
            completes fully or does not happen at all.

            If any part of the transaction fails, the entire transaction is rolled back.
            It prevents partial updates, ensuring data consistency.

            example:- consider a bank transaction

            BEGIN TRANSACTION;
            UPDATE Accounts SET Balance = Balance - 1000 WHERE AccountID = 101;  -- Debit money
            UPDATE Accounts SET Balance = Balance + 1000 WHERE AccountID = 102;  -- Credit money
            COMMIT;

'''

# Q8) what are the different levels of abstraction?
'''
ans-> In a Database Management System (DBMS), abstraction helps in hiding complex details from users and 
        providing a simplified view of data.
        
        there are mainly three levels of abstraction:-

        1. Physical Level (Lowest Level - Internal Level)
          🔹 What it Represents:
            The actual storage of data in memory (e.g., hard disk, SSDs, cloud storage).
            Focuses on how data is stored using data structures like B-trees, hashing, indexes, etc.

        2. Logical Level (Middle Level - Conceptual Level)
          🔹 What it Represents:
            Defines what data is stored and how it is related.
            Focuses on tables, schemas, relationships, constraints, and data types.

          🔹 Example:
            A university database may have this conceptual schema:

            CREATE TABLE Students (
            StudentID INT PRIMARY KEY,
            Name VARCHAR(50),
            Age INT,
            CourseID INT,
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
            );

        3. View Level (Highest Level - External Level)
           🔹 What it Represents:
            Defines different user views of the data.
            Provides data security by restricting access to sensitive information.
            A user only sees relevant data, not the entire database.
'''

# Q8) what is entity-relationship model(ER-model)?
'''
ans-> An ER Model (Entity-Relationship Model) is a high-level conceptual data model used for database design. 
      It represents real-world entities and their relationships in a structured way, making it easier to design
      a database before implementing it.

    Key Components of ER Model:
            Entities: Objects or things in the real world that have distinct identities (e.g., Student, Car, Employee).
                 Strong Entities: Exist independently (e.g., Student).
                 Weak Entities: Depend on a strong entity (e.g., Dependent in an insurance system).

            Attributes: Characteristics or properties of an entity (e.g., Student has Name, Age, Roll Number).
                 Simple Attribute: Cannot be broken down (e.g., Age).
                 Composite Attribute: Can be divided (e.g., Name → First Name + Last Name).
                 Derived Attribute: Computed from other attributes (e.g., Age from Date of Birth).
                 Multivalued Attribute: Can have multiple values (e.g., Phone Numbers).

            Relationships: Associations between entities.
                 One-to-One (1:1): Each entity is related to at most one other entity (e.g., Person ↔ Passport).
                 One-to-Many (1:M): One entity is related to many others (e.g., Teacher ↔ Students).
                 Many-to-Many (M:N): Many entities are related to many others (e.g., Students ↔ Courses).

            Keys:
                 Primary Key: Unique identifier for an entity (e.g., Student ID).
                 Foreign Key: Attribute in one table that references a primary key in another table.

            ER Diagram (ERD):An ER Model is visually represented using an ER Diagram, where:
                   Rectangles represent entities.
                   Ellipses represent attributes.
                   Diamonds represent relationships.
                   Lines connect entities to their attributes and relationships.
'''

# Q9) what are concurrency control ?
'''
ans-> Concurrency control refers to the techniques used in databases to manage multiple transactions executing 
      simultaneously while ensuring data consistency and preventing conflicts.

      Main Goals of Concurrency Control:
          Consistency: Ensuring that the database remains in a valid state despite concurrent transactions.
          Isolation:   one transaction is not interfaing other transaction.
          Deadlock Prevention: Avoiding situations where two or more transactions are waiting for each other 
                              to release resources, causing a standstill.
'''

# Q10) what are ACID property in DBMS ?
'''
ans-> ACID properties ensure the reliability and integrity of database transactions. They stand for:

          Property	              Description	                                             Example
    ----------------  --------------------------------------                   ----------------------------      
    Atomicity	     Transactions are fully completed or rolled back.      	  Money transfer: If one step fails, rollback.
    Consistency	   Database remains valid before and after a transaction.	  No negative bank balance allowed.
    Isolation	     ensures transaction will not interfaing other transaction.    Prevents double withdrawals.
    Durability	   Committed changes are permanent.	                        Flight booking stays even after a crash.
'''

# Q11) what is normalization and what are the types of normalization ?
'''
ans-> Normalization is the process of organizing a database to reduce redundancy and improve data integrity

      Types of Normalization (Normal Forms)

      1. First Normal Form (1NF) – Eliminate Repeating Groups
            ✅ Each column contains atomic values (indivisible).
            ✅ Each row has a unique identifier (Primary Key)
      
      2. Second Normal Form (2NF) – Remove Partial Dependency
            ✅ It is in 1NF.
            ✅ No Partial Dependency (Every non-key column is fully dependent on the entire primary key).

      3. Third Normal Form (3NF) – Remove Transitive Dependency
            A table is in 3NF if: ✅ It is in 2NF.
            ✅ No Transitive Dependency (Non-key attributes do not depend on other non-key attributes).

      4. Boyce-Codd Normal Form (BCNF) – Stronger 3NF
            A table is in BCNF if: ✅ It is in 3NF.
            ✅ For every functional dependency (X → Y), X should be a super key.

            📌 BCNF is used when 3NF still has anomalies due to multiple candidate keys.
'''

# Q12) what is difference between normalization and denormalization ?
'''
ans->   Feature	                      Normalization	                               Denormalization
    --------------       --------------------------------------------      ----------------------------------------
Definition	          Process of organizing data to eliminate.         Process of combining tables to improve query 
                      redundancy and improve integrity.	               performance at the cost of redundancy.

Purpose	              Reduce data redundancy and maintain consistency. Optimize read performance by reducing joins.

Data Redundancy	      Minimized (less storage used).	                 Increased (duplicate data).

Data Integrity	      High (reduces anomalies).	                       Lower (higher risk of inconsistency).

Number of Tables	    More tables (splitting data).                    Fewer tables (merging data).

Joins in Queries	    More joins required to fetch data.	             Fewer joins required, improving performance.

Performance	         Slower for read queries, but good for             Faster read queries, but 
                     inserts, updates, and deletes.	                   insert/update/delete operations are slower.

Best Used For	       Transactional databases                           Analytical databases
                     (OLTP - Online Transaction Processing).	         (OLAP - Online Analytical Processing).
'''

# Q13) Difference Between Relationship and Cardinality
'''
ans->    Feature	                     Relationship	                                   Cardinality
    -------------------      -----------------------------------------    -------------------------------------
        Definition	     Represents how two entities are associated.	     Defines the number of entities involved 
                                                                           in a relationship.

        Focus	       Qualitative (describes "what" the relationship is).   Quantitative (describes "how many").

        Representation 	  Diamond shape (e.g., "Enrolls In").              Numbers on edges (e.g., 1:1, 1:M, M:N).
        in ER Diagram

        Example	         A Student "Enrolls In" a Course.	                "One student can enroll in many courses (1:M)".

'''
# Q) what are the different types of key in DBMS ?


# Q14) what is an index ?
'''
ans-> An index in a database is a data structure that improves the speed of data retrieval operations on a table. eg:- in dsa
      from this data [1,3,4,7,3,5,2,9,7,4,3,0] you want to access 0 with linear search the T.C will be O(n). but if the data
      will be sorted then using binary search you can fetch same data fastely T.C O(log n), similarly indexing does same in database.

      types of index :-
      ------------------
      1) unique index --> A Unique Index is a type of database index that ensures all values in the indexed column(s) 
                            are distinct (no duplicate values).

      2) Clustered Index --> Sorts and stores the data rows in the table based on the index key (only one per table).

      3) Non-Clustered Index-->Creates a separate structure for quick lookups without changing the data storage order.
'''

# Q15) what is ACID property ?
'''
ans--> 
        1. Atomicity ("All or Nothing")
            A transaction is all-or-nothing.
            If any part of the transaction fails, the entire transaction is rolled back.

          Example: Transferring money between bank accounts should either complete fully or not happen at all.

        2. Consistency ("Valid State")
            A transaction must bring the database from one valid state to another.
            It must maintain rules and constraints (like unique keys, foreign keys, etc.).

          Example: If a bank transfer deducts money from one account, it must be added to another to maintain 
                    balance consistency.

        3. Isolation ("No Interference")
            Transactions are executed independently without affecting each other.
            Prevents issues like dirty reads, non-repeatable reads, and phantom reads.

          Example: If two users try to book the last train ticket at the same time, only one should succeed.

        4. Durability ("Permanent Changes")
            Once a transaction is committed, it is permanently stored.
            Even in case of a system crash, the changes should persist (using logs, backups, etc.).

          Example: After a successful order payment, even if the system crashes, the order should not disappear.
'''

# Q16) what do you mean by trigger in sql ?
'''
trigger is a special type of sql code which gives you the facility to automatically execute before and after the 
event(insert, update and delete) occure on the table.

triggers are used with these only:- 

--> before insert, after insert
--> before delete, after delete
--> before update, after update

eg:- sending welcome email to all new employees to our company.

syntax:-

CREATE TABLE IF NOT EXISTS employee (
    empId INT PRIMARY KEY,
    empName VARCHAR(50),
    empAge INT,
    empDept VARCHAR(50)
);

INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (101, 'rahul', 23, 'operator');

INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (102, 'rohan', 25, 'operator');

INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (103, 'sumit', 20, 'developer');

INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (104, 'piyush', 21, 'developer');

INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (105, 'suraj', 29, 'ceo');

select * from employee;

-- Step 1: Create the Trigger
DELIMITER $$

CREATE TRIGGER sample_trigger
BEFORE INSERT
ON employee
FOR EACH ROW
BEGIN
    SET NEW.empAge = NEW.empAge + 4;
END $$

DELIMITER ;

-- Step 2: Insert test data
INSERT INTO employee(empId, empName, empAge, empDept) 
VALUES (106, 'rajesh', 23, 'operator');

-- Step 3: Check if the trigger worked
SELECT * FROM employee;


note:- 
Understanding DELIMITER $$ in MySQL
🔹 What is DELIMITER in MySQL?
DELIMITER is a MySQL command used to change the statement terminator from the default semicolon (;) to something else (like $$).

This is necessary when writing stored procedures, triggers, or functions, which contain multiple SQL statements.
'''

# Q17) operators avilable in sql ?
'''
there are mainly 5 types of operator avilable in sql
1) arithmatic operator
2) logical operator
3) bitwise operator
4) comparision operator
5) compound operator
'''