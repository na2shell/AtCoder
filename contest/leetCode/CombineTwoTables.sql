# Write your MySQL query statement below
select FirstName, LastName, City, State
from Address
right join Person
on Address.PersonID = Person.PersonID;
