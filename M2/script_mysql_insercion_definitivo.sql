use RPM;
insert ignore RPM.CHARACTER (name,description) values
	 ("Metagross","Pesa una tonelada y tiene poderes psiquicos."),
	 ("Emme Tress","Provoca pesadillas y dolores de cabeza a quien batalla con el"),
	 ("Mike","Un tirador de elite");
select * from RPM.CHARACTER;
insert ignore USER (username,password) values
	("Rafa","P@ssw0rd"),
    ("root","root"),
    ("Pablo","Matterblast");
select * from USER;
insert ignore ADVENTURE (id_adventure,name,description) values
	(1,"El principe Ilegitimo","Eres un principe ilegitimo que debe sobrevivir a un mundo cruel y despiadado mientras te abres camino a la cima"),
    (2,"Historia del rey","Eres el REY de Drein el cual tiene un hijo ilegítimo que podría ser una amenaza");
select * from ADVENTURE;
insert ignore STEP (id_step,description,final_step,id_adventure) values 
	(1,"Eres un hijo ilegitimo de la familia real de Drein. Al ser un hijo ilegitimo de normal no tendrias que ser el sucesor pero tienes la posibilidad de serlo mediante una gerra de sucesion que eliges:",0,1),
    (2,"Al declarar tu intencion de luchar por el trono inicia una guerra en la cual tienes que que poner de tu parte la mayor cantidad de noble y soldados. Tienes la oprtunidad de ir a entablar una negociacion con un noble de grado medio y un comandante del ejercito real que eliges:",0,1),
    (3,"Al ir a negociar con el noble una parte del ejercito empiza a negociar con el principe heredero. Negociando con el noble pide una explicación de lo que aportarias al reino.Tienes la oportunidad de hacer un discurso basado en valores puramente emocionales y un discurso basado en valores puramente belicos que eliges:",0,1),
    (4,"Al escuchar el discurso que pensaste que haria que el pueblo este mas contento, te das cuenta que el noble con el que intentas negociar es una persona que solo le interesa el poder y su propio beneficio y intentas rapidamente entablar una aliaza con el comandante del ejercito pero al llegar te encuentras un poco de sangre. Tienes la oportunidad de avanzar para ver que a pasado o huir del sitio que eliges:",0,1),
    (5,"Al intentar investigar ves que estas encerrado y te das cuenta que es una trampa derrepente aparece un asesino y te corta la cabeza sin siquiera poder hacer nada. Fin",1,1),
    (6,"Al intentar huir ves estas encerrado y te das cuenta que es una trampa derrepente aparece un asesino y te corta la cabeza sin siquiera poder hacer nada. Fin",1,1),
    (7,"Al escuchar el dicurso el noble se le ponen los ojos como platos y entabla una alianza. Al entablar alianza con aquel noble conigues mas influencia entre los amigos del ya comentado noble con los que aparte te dan una ayuda al intentar difamar al principe legitimo. Empiza la guerra y entre todo aquel caos tienes la opcion de matar a el principe legitimo o dejarlo vivir que eliges:",0,1),
    (8,"Al matar al principe ganas la guerra y te conviertes en el proximo rey de drein. FIN.",1,1),
    (9,"Al dejarlo vivir y darle la espalda al principe el te clava la espada por detras haciendo que mueras. FIN.",1,1),
    (10,"Al ir a negociar con el comandante del ejercito empiza a negociar con el principe heredero. Negociando con el noble pide una explicación de lo que aportarias al reino.Tienes la oportunidad de hacer un discurso vasado en valores puramente emocionales o puramente belicos. Que discurso eliges:",0,1),
    (11,"Al hacer tu discurso ves que el comandante sigue indiferente hacia ti. Derrepente irrumpe el principe Jaffar  Fraynn y la actitud del comandante cambia drasticamente y te das cuenta de que estan ya compinchados y que desde un principio era una trampa para asi amenzazarte para dejar de intentar ser el proximo rey. Tines la oportunidad de negarte rotundamente o hacerles caso. Que eliges:",0,1),
    (12,"Al negarte el principe Jaffar sin miramientos le ordena al comandante que te mate. Fin",1,1),
    (13,"Al hacerles caso igualmente el principe hace que el comandante te cortara una pierna para asi asegurarse que no intentaras despues volver a intentar reclamar el trono. Sin pierna y la emoción de odio y frustración hace que llegues a un estado mental de locura donde en uno de tus ataques te golpeas contra una pared de tal manera que te abres la cabeza y mueres en el acto. Fin",1,1),
    (14,"Al dar a conocer tu indiferencia ante el trono la gente empieza a hablar mal de ti. AL enteretarte de lo que habla el pueblo tienes la oportunidad de enfadarte con el pueblo o quedar indiferente que eliges:",0,1),
    (15,"Al enterarte de todos los comentarios de la gente te enfadas de tal manera que sin darte cuenta en un arrebato de ira le das una paliza casi mortal a un plebeyo y entonces la guardia real te aprisiona. En el Juicio tu propio padre reconoce lo mal hijo que eres y se siente avergonzado y entonces con una cara de decepcion ordena tu ejecución. Fin",1,1),
    (16,"Al quedar indiferente cada vez el pueblo se rie mas de ti hasta que llega un momento que no puedes mas y te suicidas. Fin",1,1),
    (17,"Al huir del reino para buscar otro reino para que te acoja hay un asalto al carruaje en el que ibas. Tienes la oportunidad de luchar contra los bandidos, intentar negociar o huir dejando atras a todo el mundo que eliges",0,1),
    (18,"al empezara a luchar contra los bandidos, en medio de la pelea, uno de los bandidos te agarra por la espalda y otro por delante te corta la cabeza. Fin",1,1),
    (19," Al intentar negociar ves que no sirve para nada y entonces te esclavizan hasta tu muerte. Fin",1,1),
    (20,"Al huir envian en tu busqueda un hombre a caballo y mientras se va acercando cada vez , recuerdas todas tus malas decisiones... Acaban con tu vida  después de muchas horas huyendo. FIN",1,1),
    (21,"Eres el rey de Drein, un día te llegan noticias sobre un hijo ilegítimo que podía intentar reclamar el trono, ¿qué decides hacer?",0,2),
    (22,"Mandas llamar al heredero ilegítimo para hablar con él, se presenta como Adolfo",0,2),
    (23,"Responde que pretende hacerse con el trono una vez mueras, que él es el auténtico heredero.",0,2),
    (24,"Le dices que si prueba tu paternidad tendrá opciones para acceder al trono legalmente, él te lo agradece, dice que traerá pruebas y se marcha. Al parecer vuelve con la prueba de paternidad y se confirma que él es heredero legítimo al ser su hijo pero con su primera esposa que supuestamente no podía tener hijos. Al cederle el trono el heredero se convierte en un rey probablemente mejor incluso que tu. Fin",1,2),
    (25,"Le explicas que tu verdadero hijo es el que ocupará el trono, que él no es más que un usurpador, al intimidarlo de esa forma te deja enpaz a ti y a toda la familia real. Fin",1,2),
    (26,"Responde que tiene pruebas de tu paternidad y que seguirá usando tú apellido, él había venido con buenas intenciones pero ahora tratará de hacerse con el reino de Dreinn por las malas.",0,2),
    (27,"Hijo ilegítimo asesinado con éxito, se acabó el problema.Fin",1,2),
    (28,"Te contesta que tiene un documento guardado en su casa que puede probar lo que dice, pero que no te contará más, se marcha del castillo.",0,2),
    (29,"Tus guardias lo encuentran antes de que coja las pruebas y lo encierran, tu reino está a salvo, tú ganas.FIN",1,2),
    (30,"Al quedarse a esperar a ver que pasa el heredero ilegítimo consigue pruebas y hace un par de líos legales para sacarte del trono.FIN",1,2),
    (31,"Las disculpas no sirven de mucho, Adolf se marcha del castillo lleno de ira y sin respetarte demasiado, vuelve más tarde con sus soldados y te mata.FIN",1,2),
    (32,"Acepta el trato y se convierte en un tirano, abunda el terror en las calles, eres de los primeros en morir.",1,2),
    (33,"Decides ignorar la noticia, tachándola de un simple rumor, pero esta va ganando fuerza y el heredero ilegítimo va ganando seguidores por su ideología y hay disturbios en las calles.",0,2),
    (34,"Este hombre se presenta en el castillo con unos guardaespaldas diciendo que se llama Adolf Fraynn, y exige que le des tu reino de inmediato:",0,2),
    (35,"Resulta que darle el reino no ha sido la mejor decisión. Se vuelve un tirano y te mata en cuanto puede",1,2),
    (36,"Al tratar de razonar con él comencáis a negociar",0,2),
    (37,"Al ofrecerle ser duque, el acepta pero con la condición de que le tenga en cuenta a la hora de abdicar el trono. Fin",1,2),
    (38,"Al ofrecerle vivir en palacio, el lleno de ira te empieza a decir que no necesita vivir en palacio ya que va a ser su palacio al matarte y de un momento a otro de repente ves que el suelo se acerca demasiado rápido. (te han cortado la cabeza y has muerto). Fin.",1,2),
    (39,"Al no ofrecerle nada se lo toma como un insulto y te mata sin compasión haciendo una ejecución pública. Fin",1,2),
    (40,"Hijo ilegítimo asesinado con éxito, se acabó el problema.FIN",1,2),
    (41,"Al mandar a las fuerzas del orden te quedas desprotegido y aprovechan ese momento para infiltrase en el castillo y matarte utilizando veneno. Fin",1,2),
    (42,"Al seguir ignorando la noticia derrepente el pueblo junto al heredero ilegitimo irrumpen dentro de castillo asi haciendo un complot contra la corona y matarte para hacer rey al heredero ilegitimo. Fin",1,2),
    (43,"Hijo ilegítimo asesinado con éxito, se acabó el problema.FIN",1,2);
select * from STEP;
insert ignore ANSWER (id_answer,description,id_current_step,id_step_resolution) values
	(1,"Entablar una gerra contra el principe sucesor",1,2),
    (2,"Ser indiferente ante el trono",1,14),
    (3,"Huir a otro reino",1,17),
    (4,"Noble de grado medio",2,3),
    (5,"Comandante del ejercito real",2,10),
    (6,"Discurso basado en emociones",3,4),
    (7,"Discurso belico",3,7),
    (8,"Ver que a pasado",4,5),
    (9,"huir",4,6),
    (10,"matar al principe",7,8),
    (11,"dejarlo vivir",7,9),
    (12,"Discurso emocional",10,11),
    (13,"Discurso belico",10,11),
    (14,"negarte",11,12),
    (15,"Hacerles caso",11,13),
    (16,"enfadarte con el pueblo",14,15),
    (17,"quedar indiferente",14,16),
    (18,"Luchar contra los bandidos",17,18),
    (19,"Intentar negociar",17,19),
    (20,"Huir",17,20),
    (21,"Tratar de conocer al hijo",21,22),
    (22,"Ignorar la noticia",21,33),
    (23,"Mandarlo asesinar",21,43),
    (24,"Le preguntas cuáles son sus intenciones hacia el trono.",22,23),
    (25,"Le ordenas que deje de utilizar tu apellido, le dices que no es tu hijo.",22,26),
    (26,"Le ofreces tu reino.",22,32),
    (27,"Acercamiento amistoso.",23,24),
    (28,"Acercamiento hostil.",23,25),
    (29,"Mandarlo asesinar antes de que salga del castillo",26,27),
    (30,"Preguntar por las pruebas",26,28),
    (31,"Disculparte",26,31),
    (32,"Mandar que lo paren antes de que vaya a recoger las pruebas.",28,29),
    (33,"Esperar a ver que pasa.",28,30),
    (34,"Mandar llamar a este heredero ilegítimo",33,34),
    (35,"Mandar a las fuerzas del orden que acaben con los disturbios",33,41),
    (36,"Seguir ignorando la noticia",33,42),
    (37,"Acceder a darle el reino",34,35),
    (38,"Negarte y tratar de razonar",34,36),
    (39,"Mandar a los guardias matarlo",34,40),
    (40,"Ofrecerle ser duque",36,37),
    (41,"Ofrecerle vivir en el palacio",36,38),
    (42,"No ofrecer nada",36,39);
select * from ANSWER;
insert ignore GAME (id_game,id_adventure,id_user,id_character) values
	(1,1,1,1);
select * from GAME;
insert ignore HISTORY (id_game,id_step,id_answer) values 
	(1,1,1),
    (1,2,4),
    (1,4,8);
select * from HISTORY;
insert ignore ARE_AVAILABLE (id_character,id_adventure) values
	(1,1),
    (1,2),
    (2,2),
    (3,1);
select * from ARE_AVAILABLE;