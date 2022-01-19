create database if not exists RPM;
use RPM;
create table if not exists USER (
	id_user int ,
	username varchar(15) ,
	password varchar(40) ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists RPM.CHARACTER (
	id_character int ,
    name varchar(40) ,
    description varchar(100),
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists ADVENTURE (
	id_adventure int ,
    name varchar(40) ,
    description varchar(100) ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists STEP (
	id_step int ,
    final_step boolean,
    description varchar(100)  ,
    id_adventure int ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists ANSWER (
	id_answer int ,
    description varchar(100),
    id_step_resolution int ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);

create table if not exists GAME (
	id_game int ,
    id_adventure int ,
    id_user int ,
    id_character int ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists HAS (
	id_adventure int ,
    id_character int ,
    date_creation timestamp,
    user_modified varchar(15),
    date_modified date
);
create table if not exists HISTORY (
	id_game int,
    id_answer int,
    id_step int
);