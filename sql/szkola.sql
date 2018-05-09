DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
	egzHum NUMERIC NOT NULL DEFAULT 0,
	egzMat NUMERIC NOT NULL DEFAULT 0,
	egzJez NUMERIC NOT NULL DEFAULT 0,
	FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)
	);

DROP TABLE IF EXISTS tbKlasy;
CREATE TABLE tbKlasy
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
klasa TEXT,
rokNaboru INTEGER,
rokMatury INTEGER
);

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1B', 2017, 2020);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '2A', 2016, 2019);

INSERT INTO tbUczniowie VALUES (NULL, 'Adam', 'Słodowy', 0, 2, 68, 80, 87);
INSERT INTO tbUczniowie VALUES (NULL, 'Nikola', 'Chmiel', 1, 1, 98, 86, 90);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;