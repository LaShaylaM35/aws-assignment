CREATE TABLE persons (
    id serial primary key,
    first_name varchar(50)NOT NULL,
    last_name varchar(50),
    address varchar(100),
    age int
);


drop table persons;

