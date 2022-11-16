--  lists all Comedy shows in the database hbtn_0d_tvshows.
--The tv_genres table contains only one record where name = Comedy

SELECT s.title FROM tv_show_genres sg
JOIN tv_genres g ON sg.genre_id = g.id
JOIN tv_shows s ON sg.show_id = s.id
WHERE g.name = "Comedy"
ORDER BY s.title ASC;