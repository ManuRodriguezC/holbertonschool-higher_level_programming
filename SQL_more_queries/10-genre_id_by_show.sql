-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT s.title, g.genre_id FROM tv_shows s LEFT JOIN tv_show_genres g 
ON s.id = g.show_id WHERE genre_id != "" ORDER BY title, genre_id ASC;