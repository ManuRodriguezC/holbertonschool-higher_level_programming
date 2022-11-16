--  lists all shows that not contein a genre contained in the database hbtn_0d_tvshows.

SELECT s.title, g.genre_id FROM tv_shows s LEFT JOIN tv_show_genres g 
ON s.id = g.show_id WHERE genre_id IS NULL ORDER BY title, genre_id ASC;