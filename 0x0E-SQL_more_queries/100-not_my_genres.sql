-- All genres not linked to the Dexter show
USE `hbtn_0d_tvshows`;
SELECT `name`
FROM `tv_genres`
WHERE `name` NOT IN (
    SELECT tv_genres.name
    FROM `tv_genres`
    LEFT JOIN `tv_show_genres`
    ON tv_show_genres.genre_id = tv_genres.id
    LEFT JOIN `tv_shows`
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name