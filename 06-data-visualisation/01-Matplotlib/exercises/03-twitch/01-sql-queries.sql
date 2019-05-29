select * from stream limit 10;
select * from chat limit 10;

/* unique games and channels */
select distinct game from stream;
select distinct channel from stream;

/* what are the most popular games in strem table */
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;


/* Where are these LoL stream viewers located? */
select country, count(*)
from stream
where game = 'League of Legends'
group by 1
order by 2 desc
limit 10;



/* Create a list of players and their number of streamers. */
select player, count(*)
from stream
group by 1
order by 2 desc;


/* group gmaes by genres, crete a new column 'genre' */
SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;


SELECT time
FROM stream
LIMIT 10;

/*

For strftime(__, timestamp):
%Y returns the year (YYYY)
%m returns the month (01-12)
%d returns the day of the month (1-31)
%H returns 24-hour clock (00-23)
%M returns the minute (00-59)
%S returns the seconds (00-59)

if time format is YYYY-MM-DD HH:MM:SS.
The HH is the hour of the day, from 0 to 23.
The MM is the minute of the hour, from 0 to 59.
The SS is the seconds within a minute, from 0 to 59.
*/

SELECT time, strftime('%S', time) AS seconds
FROM stream
GROUP BY 1
LIMIT 20;


/* return the time, view count for your country */

select strftime('%H', time) as 'Hours', count(*) as 'Count'
from stream
where country = 'US'
group by 1;


/* join the stream and chat tables via 'device_id'*/
SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;
