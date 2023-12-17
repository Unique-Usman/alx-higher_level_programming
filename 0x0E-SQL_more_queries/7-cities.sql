create database if not exists hbtn_0d_usa;
use hbtn_0d_usa;
create table if not exists cities
(id int auto_increment not null primary key,
name varchar(256) not null,
state_id int not null, foreign key(state_id) references states(id));
