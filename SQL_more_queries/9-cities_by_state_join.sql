-- lists all cities contained in the database hbtn_0d_usa.

SELECT FROM c.id, c.name, s.name cities c LEFT JOIN states s ON c.state_id = s.id ORDER BY c.id ASC;