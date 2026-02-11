You are working with a database used by a university library system.  
The system tracks library members, books, and borrowing activity.

The database contains the following tables:

members(<u>member_id</u>, member_name, join_date)  
books(<u>book_id</u>, title, author)  
loans(<u>loan_id</u>, member_id, book_id, loan_date, return_date)

---

a) For each pair of tables below, state the type of relationship  
(one-to-one, one-to-many, or many-to-many) and briefly explain your reasoning.

i. Members and loans [2]  --> one-to-many
ii. Books and loans [2]  --> many-to-many
iii. Members and books [2]  --> one-to-many

---

b) A query joins members to loans using an INNER JOIN.

i. Explain what happens to members who have never borrowed a book. [2]  
    --> Not included in the displayed data
ii. Explain how the results of the query would change if a LEFT JOIN were used instead. [2]  
    --> The displayed data would show members who have never borrowed a book
---

c) The head librarian would like to see how many books have been borrowed by each library member.

i. Write an SQL query which would show the name of each library member and how many loans they have taken out. [5]  

    SELECT M.member_name, COUNT(L.loan_id)
    FROM members M
    LEFT JOIN loans L ON M.member_id = L.member_id
    ORDER BY M.member_id;
---

d) The head librarian asks:  
“Why don’t you store the book title with the loan? Wouldn’t that make it easier to see the data?”

i. Explain, using appropriate non-technical language, why this would be bad database design. [5]
  --> Because there could be multiple books with each loan