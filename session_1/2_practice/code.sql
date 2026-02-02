-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
-- 1. **List all loans**  
-- Show book title, member name, and loan date.
SELECT Books.title, Members.name, Loans.loan_date FROM Loans JOIN Books ON Loans.book_id = Books.id JOIN Members ON Loans.member_id = Members.id;

-- 2. **Books and loans**  
-- List all books and any loans associated with them.
SELECT Books.*, Loans.* FROM Books LEFT JOIN Loans ON Books.id = Loans.book_id;

-- 3. **Branches and books**  
-- List all library branches and the books they hold.
SELECT LibraryBranch.name, Books.title FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id;

-- 4. **Branch book counts**  
-- Show each library branch and the number of books it holds.
SELECT LibraryBranch.name, Count(Books.id) FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id GROUP BY LibraryBranch.id, LibraryBranch.name;

-- 5. **Branches with more than 7 books**  
-- Show branches that hold more than 7 books.
SELECT LibraryBranch.name, Count(Books.id) AS TotalBooks FROM LibraryBranch LEFT JOIN Books ON LibraryBranch.id = Books.branch_id GROUP BY LibraryBranch.id, LibraryBranch.name HAVING COUNT(Books.id) > 7;

-- 6. **Members and loans**  
-- List all members and the number of loans they have made.
SELECT Members.name, Count(Loans.id) AS TotalLoans FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id GROUP BY Members.id;

-- 7. **Members who never borrowed**  
-- Identify members who have never borrowed a book.
SELECT Members.name, Count(Loans.id) AS TotalLoans FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id GROUP BY Members.id HAVING Count(Loans.id) = 0;

-- 8. **Branch loan totals**  
-- For each library branch, show the total number of loans for books in that branch.
SELECT LB.name, Count(Loans.id) AS TotalLoans FROM LibraryBranch as LB LEFT JOIN Books ON LB.id = Books.branch_id LEFT JOIN Loans ON Books.id = Loans.book_id GROUP BY LB.id;

-- 9. **Members with active loans**  
-- List members who currently have at least one active loan.
SELECT Members.Name, Count(Loans.id) FROM Members LEFT JOIN Loans ON Members.id = Loans.member_id GROUP BY Members.id HAVING Count(Loans.id) > 0;

-- 10. **Books and loans report**  
-- Show all books and all loans, including books that were never loaned. Include a column classifying each row as “Loaned book” or “Unloaned book.”. You will need to look up how to do this (hint: a case statement would work).
SELECT Books.title, Loans.id,
    CASE
        WHEN Loans.id IS NULL THEN 'Unloaned Book'
        ELSE 'Loaned Book'
    END AS LoanStatus
FROM Books LEFT Join Loans ON Books.id = Loans.book_id;