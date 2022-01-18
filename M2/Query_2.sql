select username, count(username) as "PARTIDAS JUGADAS"
from GAME
group by username
order by count(username) desc limit 1;