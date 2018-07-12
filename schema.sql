 drop table if exists services;
    create table services (
    id integer primary key autoincrement,
    name text varchar(100),
    date datetime,
    location text varchar(50),
    minister text varchar(50),
    link text varchar(50),
    expiration text varchar(50),
    comment text varchar(1000)
);

 drop table if exists assignees;
    create table assignees (
    id integer primary key autoincrement,
    name text varchar(20),
    service_id foreign key
);