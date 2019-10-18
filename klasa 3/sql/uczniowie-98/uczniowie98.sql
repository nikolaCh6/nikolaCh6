CREATE TABLE uczniowie (
    id_ucz CHAR(8) PRIMARY KEY,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
    klasa CHAR (5) DEFAULT ''
);
-- ang. constraints
CREATE TABLE przedmioty(
    id_przedm INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(70) NOT NULL CHECK (nazwa <> '')
);

CREATE TABLE oceny(
    id_oceny INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    id_ucz CHAR(8),
    id_przed INTEGER,
    ocena DECIMAL(3,2)
    FOREIGN KEY (id_ucz) REFERENCES uczniowie (id_ucz)
    ON DELETE CASCADE
    FOREIGN KEY (id_przedm) REFERENCES przedmioty (id_przedm)
    ON DELETE SET NULL
);
 

