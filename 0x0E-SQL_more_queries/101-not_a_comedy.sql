-- not a comedy show, All shows that aren't comedy shows
SELECT `title`
FROM `tv_shows`
WHERE `title` NOT IN (
    SELECT tv_shows.title
    FROM `tv_shows`
    LEFT JOIN `tv_show_genres`
    ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN `tv_genres`
    ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title