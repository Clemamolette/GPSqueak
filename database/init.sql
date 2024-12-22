

CREATE TABLE IF NOT EXISTS coordinates(id SERIAL PRIMARY KEY, id_mouse FOREIGN KEY(mouses.id), latitude FLOAT, longitude FLOAT, t_stamp INT);

CREATE TABLE IF NOT EXISTS mouses(id SERIAL PRIMARY KEY, ip VARCHAR(50), name VARCHAR(100));