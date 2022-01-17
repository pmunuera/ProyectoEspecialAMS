create database if not exists PROYECTO;
use PROYECTO;
create table if not exists USER (
	id_user int unsigned auto_increment primary key,
	username varchar(15) not null,
	password varchar(40) not NULL
);
create table if not exists PROYECTO_CHARACTER (
	id_character int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name varchar(40) not null unique,
    description varchar(100)
);
create table if not exists ADVENTURE (
	id_adventure int unsigned auto_increment primary key,
    name varchar(40) not null unique,
    description varchar(100) null
);
create table if not exists STEP (
	id_step int unsigned auto_increment primary key,
    final_step boolean,
    description varchar(100) not null ,
    id_adventure int unsigned,
    constraint FK_ADVENTURE_STEP foreign key (id_adventure) references ADVENTURE(id_adventure)
);
create table if not exists ANSWER (
	id_answer int unsigned auto_increment primary key,
    description varchar(100) not null,
    id_step_resolution int unsigned,
    constraint FK_ANSWER_STEP foreign key (id_step_resolution) references STEP(id_step)
);

create table if not exists GAME (
	id_game int unsigned auto_increment primary key,
    date timestamp,
    id_adventure int unsigned not null,
    username int unsigned not null,
    id_character int unsigned not null,
    id_step int unsigned not null,
    constraint FK_GAME_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
    constraint FK_GAME_USER foreign key (username) references USER(id_user),
    constraint FK_GAME_CHARACTER foreign key (id_character) references PROYECTO_CHARACTER(id_character),
    constraint FK_GAME_STEP foreign key (id_step) references STEP(id_step)
);
create table if not exists HAS (
	id_adventure int unsigned not null,
    id_character int unsigned not null,
    constraint FK_HAS_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
    constraint FK_HAS_CHARACTER foreign key (id_character) references PROYECTO_CHARACTER(id_character)
);