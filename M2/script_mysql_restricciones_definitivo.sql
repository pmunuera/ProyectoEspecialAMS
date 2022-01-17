use PROYECTO;
ALTER DATABASE PROYECTO CHARACTER SET utf8 COLLATE utf8_general_ci;
alter table USER modify id_user int unsigned auto_increment primary key;
alter table USER modify username varchar(15) not null;
alter table USER modify password varchar(40) not null;
alter table USER add constraint unique_user unique (username);
alter table USER modify date_creation timestamp default localtimestamp();

alter table PROYECTO_CHARACTER modify id_character int UNSIGNED AUTO_INCREMENT PRIMARY KEY;
alter table PROYECTO_CHARACTER modify name varchar(40) not null;
alter table PROYECTO_CHARACTER add constraint unique_name unique (name);
alter table PROYECTO_CHARACTER modify date_creation timestamp default localtimestamp();

alter table ADVENTURE modify id_adventure int unsigned auto_increment primary key;
alter table ADVENTURE modify name varchar(40) not null unique;
alter table ADVENTURE modify description varchar(100) not null;
alter table ADVENTURE modify date_creation timestamp default localtimestamp();

alter table STEP modify id_step int unsigned auto_increment primary key;
alter table STEP modify description varchar(100) not null;
alter table STEP modify id_adventure int unsigned;
alter table STEP add constraint FK_ADVENTURE_STEP foreign key (id_adventure) references ADVENTURE(id_adventure);
alter table STEP modify date_creation timestamp default localtimestamp();

alter table ANSWER modify id_answer int unsigned auto_increment primary key;
alter table ANSWER modify description varchar(100) not null;
alter table ANSWER modify id_step_resolution int unsigned;
alter table ANSWER add constraint FK_ANSWER_STEP foreign key (id_step_resolution) references STEP(id_step);
alter table ANSWER modify date_creation timestamp default localtimestamp();

alter table GAME modify id_game int unsigned auto_increment primary key;
alter table GAME modify id_adventure int unsigned not null;
alter table GAME modify username int unsigned not null;
alter table GAME modify id_character int unsigned not null;
alter table GAME modify id_step int unsigned not null;
alter table GAME add constraint FK_GAME_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure);
alter table GAME add constraint FK_GAME_USER foreign key (username) references USER(id_user);
alter table GAME add constraint FK_GAME_CHARACTER foreign key (id_character) references PROYECTO_CHARACTER(id_character);
alter table GAME add constraint FK_GAME_STEP foreign key (id_step) references STEP(id_step);
alter table GAME modify date_creation timestamp default localtimestamp();

alter table HAS modify id_adventure int unsigned not null;
alter table HAS modify id_character int unsigned not null;
alter table HAS add constraint FK_HAS_ADVENTURE foreign key (id_adventure) references ADVENTURE(id_adventure);
alter table HAS add constraint FK_HAS_CHARACTER foreign key (id_character) references PROYECTO_CHARACTER(id_character);
alter table HAS modify date_creation timestamp default localtimestamp();