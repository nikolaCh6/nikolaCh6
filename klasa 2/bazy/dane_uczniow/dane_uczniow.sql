DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie (
	numer_ucznia INTEGER PRIMARY KEY,
	nazwisko TEXT,
	pierwsze_imie TEXT,
    drugie_imie TEXT
);

DROP TABLE IF EXISTS tbDane_os;
CREATE TABLE tbDane_os (
	numer_ucznia REFERENCES tbUczniowie(numer_ucznia),
	dzien_urodzenia INTEGER,
	miesiac_urodzenia INTEGER,
    rok_urodzenia INTEGER,
    miejsce_urodzenia TEXT,
    wojewodztwo_urodzenia TEXT
);

DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny (
	numer_ucznia REFERENCES tbUczniowie(numer_ucznia,
	zachowanie TEXT
	religia_etyka DECIMAL DEFAULT NULL,
    jpolski DECIMAL DEFAULT NULL,
    jangielski DECIMAL DEFAULT NULL,
    jniemiecki DECIMAL DEFAULT NULL,
    matematyka DECIMAL DEFAULT NULL,
    historia DECIMAL DEFAULT NULL,
    geografia DECIMAL DEFAULT NULL,
    biologia DECIMAL DEFAULT NULL,
    fizyka DECIMAL DEFAULT NULL,
    chemia DECIMAL DEFAULT NULL,
    technika DECIMAL DEFAULT NULL,
    informatyka DECIMAL DEFAULT NULL,
    plastyka DECIMAL DEFAULT NULL,
    po DECIMAL DEFAULT NULL,
    wf DECIMAL DEFAULT NULL
);
