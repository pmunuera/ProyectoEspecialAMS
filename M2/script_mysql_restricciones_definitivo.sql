use RPM;
ALTER DATABASE RPM CHARACTER SET utf8 COLLATE utf8_general_ci;

alter table USER 
	modify id_user int unsigned auto_increment primary key,
	modify username varchar(15) not null,
	modify password varchar(40) not null,
	add constraint unique_user unique (username),
	modify date_creation timestamp default localtimestamp();

alter table RPM.CHARACTER 
	modify id_character int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	modify name varchar(40) not null,
	add constraint unique_name unique (name),
	modify date_creation timestamp default localtimestamp();

alter table ADVENTURE 
	modify id_adventure int unsigned auto_increment primary key,
	modify name varchar(40) not null unique,
	modify description varchar(100) not null,
	modify date_creation timestamp default localtimestamp();

alter table STEP 
	modify id_step int unsigned auto_increment primary key,
	modify description varchar(100) not null,
	modify id_adventure int unsigned,
	add constraint FK_ADVENTURE_STEP foreign key (id_adventure) references ADVENTURE(id_adventure),
	modify date_creation timestamp default localtimestamp();

alter table ANSWER 
	modify id_answer int unsigned auto_increment primary key,
	modify description varchar(100) not null,
	modify id_step_resolution int unsigned,
	add constraint FK_ANSWER_STEP foreign key (id_step_resolution) references STEP(id_step),
	modify date_creation timestamp default localtimestamp();

alter table GAME 
	modify id_game int unsigned auto_increment primary key,
	modify id_adventure int unsigned not null,
	modify username int unsigned not null,
	modify id_character int unsigned not null,
	modify id_step int unsigned not null,
	add constraint FK_GAME_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
	add constraint FK_GAME_USER foreign key (username) references USER(id_user),
	add constraint FK_GAME_CHARACTER foreign key (id_character) references RPM.CHARACTER(id_character),
	add constraint FK_GAME_STEP foreign key (id_step) references STEP(id_step),
	modify date_creation timestamp default localtimestamp();

alter table HAS 
	modify id_adventure int unsigned not null,
	modify id_character int unsigned not null,
	add constraint FK_HAS_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure),
	add constraint FK_HAS_CHARACTER foreign key (id_character) references RPM.CHARACTER(id_character),
	modify date_creation timestamp default localtimestamp();