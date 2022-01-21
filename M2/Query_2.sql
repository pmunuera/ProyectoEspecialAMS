select u.username, count(g.id_user) as "PARTIDAS JUGADAS"
from GAME g inner join USER u on u.id_user=g.id_user
group by g.id_user
order by count(g.id_user) desc limit 1 ;