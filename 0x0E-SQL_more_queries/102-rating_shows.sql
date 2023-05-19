-- show overall ratings
USE `hbtn_0d_tvshows_rate`;
SELECT tv_shows.title, SUM(`rate`) AS rating
FROM `tv_show_ratings`
JOIN `tv_shows`
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY `show_id`
ORDER BY rating DESC