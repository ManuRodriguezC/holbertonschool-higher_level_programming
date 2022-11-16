-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>

SELECT g.name AS genre, count(s.genre_id) AS number_of_shows FROM tv_genres g JOIN tv_show_genres s ON id = genre_id
GROUP BY g.name
ORDER BY count(s.genre_id) DESC;