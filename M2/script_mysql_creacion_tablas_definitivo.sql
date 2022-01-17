create database if not exists PROYECTO;
use PROYECTO;
create table if not exists USER (
	id_user int ,
	username varchar(15) ,
	password varchar(40) 
);
create table if not exists PROYECTO_CHARACTER (
	id_character int ,
    name varchar(40) ,
    description varchar(100)
);
create table if not exists ADVENTURE (
	id_adventure int ,
    name varchar(40) ,
    description varchar(100) 
);
create table if not exists STEP (
	id_step int ,
    final_step boolean,
    description varchar(100)  ,
    id_adventure int 
);
create table if not exists ANSWER (
	id_answer int ,
    description varchar(100),
    id_step_resolution int 
);

create table if not exists GAME (
	id_game int ,
    date timestamp,
    id_adventure int ,
    username int ,
    id_character int ,
    id_step int 
);
create table if not exists HAS (
	id_adventure int ,
    id_character int 
);