adventures={id_adventure:{'Name': adventure_name,
                          'Description':adventure_description,
                          'Characters': adventure_characters}
            }
characters={id_character:character_name}

Answers_ByStep_Adventure={{idAnswers_ByStep_Adventure, idByStep_Adventure}:{
                            'Description':description,
                            'Resolution_Answer':Resolution_Answer},
                            'NextStep_Adventure':NextStep}
BySteps_Adventure={id_ByStep_Adventure:{'Description':Description,
                                       'answers_in_step':answers_in_step,
                                       "Final_Step":Final_Step}
                  }
replayAdventures={idGame:{'idUser':id_user,'Username':username,
                          'IdAdventure':id_adventure,
                          'Name':adventure_name,
                          'date':date,
                          'idCharacter':id_character,
                          'CharacterName':character_name}
                  }