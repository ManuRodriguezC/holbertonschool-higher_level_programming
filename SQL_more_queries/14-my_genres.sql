-- That uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT g.name FROM tv_show_genres sg
JOIN tv_shows s ON s.id = sg.show_id
JOIN tv_genres g ON g.id = genre_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;