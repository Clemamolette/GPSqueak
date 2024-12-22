

CREATE TABLE IF NOT EXISTS mouses(id SERIAL PRIMARY KEY, ip VARCHAR(50), name VARCHAR(100));

CREATE TABLE IF NOT EXISTS coordinates(id SERIAL PRIMARY KEY, id_mouse INT, latitude FLOAT, longitude FLOAT, t_stamp TIMESTAMP, FOREIGN KEY(id_mouse) REFERENCES mouses(id));