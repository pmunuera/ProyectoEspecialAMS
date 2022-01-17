create table if not exists USERS (
	id_user int unsigned auto_increment primary key,
	username varchar(15) not null,
	password varchar(40) not NULL
);
create table if not exists CHARACTERS (
	id_characters int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name varchar(40) not null unique,
    description varchar(100) null
);
create table if not exists ADVENTURE (
	id_adventure int unsigned auto_increment primary key,
    name varchar(40) not null unique,
    description varchar(100) null
);
create table if not exists STEPS (
	id_steps int unsigned auto_increment primary key,
    final_step boolean,
    description varchar(100) not null ,
    id_adventure int unsigned,
    constraint FK_ADVENTURE_STEPS foreign key (id_adventure) references ADVENTURE(id_adventure)
);
create table if not exists ANSWERS (
	id_answers int unsigned auto_increment primary key,
    description varchar(100) not null,
    id_steps_resolution int unsigned,
    constraint FK_ANSWER_STEPS foreign key (id_steps_resolution) references STEPS(id_steps)
);

create table if not exists GAME (
	id_game int unsigned auto_increment primary key,
    date timestamp,
    id_adventure int unsigned not null,
    username int unsigned not null,
    id_characters int unsigned not null,
    constraint FK_GAME_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
    constraint FK_GAME_USERS foreign key (username) references USERS(id_user),
    constraint FK_GAME_CHARACTERS foreign key (id_characters) references CHARACTERS(id_characters)
);
create table if not exists HAS (
	id_adventure int unsigned not null,
    id_characters int unsigned not null,
    constraint FK_HAS_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
    constraint FK_HAS_CHARACTERS foreign key (id_characters) references CHARACTERS(id_characters)
);
create table if not exists COMPOSES (
	id_game int unsigned not null,
    id_steps int unsigned not null,
    constraint FK_STEPS_COMPOSES foreign key (id_steps) references STEPS(id_steps),
    constraint FK_GAME_COMPOSES foreign key (id_game) references GAME(id_game)
);