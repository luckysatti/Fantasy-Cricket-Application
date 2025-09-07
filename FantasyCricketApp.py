import sqlite3
Cricket=sqlite3.connect('FantasyCricketApp.db')
cursor=Cricket.cursor()

#CREATING MATCH TABLE
cursor.execute('''CREATE TABLE MATCH(
PLAYER STRING PRIMARY KEY,
SCORE INTEGER,
BALLSFACED INTEGER,
FOURS INTEGER,
SIXES INTEGER,
BOWLED INTEGER,
MAIDEN INTEGER,
GIVEN INTEGER,
WICKETS INTEGER,
CATCHES INTEGER,
STUMPINGS INTEGER,
RUNOUTS INTEGER );''')
Cricket.commit()

#CREATING TEAMS TABLE
cursor.execute('''CREATE TABLE TEAMS(
NAME STRING,
PLAYERS STRING,
VALUE INTEGER);''')
Cricket.commit()

#CREATING STATS TABLE
cursor.execute('''CREATE TABLE STATS(
PLAYER STRING PRIMARY KEY,
MATCHES INTEGER,
RUNS INTEGER,
HUNDREDS INTEGER,
FIFTIES INTEGER,
VALUE INTEGER,
CATEGORY STRING);''')
Cricket.commit()

#POPULATING MATCH TABLE
cursor.execute('''INSERT INTO MATCH
VALUES('Kohli',     102,    98,    8,    2,    0,    0,    0,    0,    0,    0,    1);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Yuvraj',    12,    20,    1,    0,	   48,	 0,	   36,	 1,   0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Dhawan',	32,	   35,	  4,	0,	   0,	 0,	   0,	 0,	  0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Dhoni',	    56,    45,	  3,	1,	   0,    0,	   0,	 0,	  3,	 2,	   0);''')   
cursor.execute('''INSERT INTO MATCH
VALUES('Axar',	    8,	   4,	  2,	0,	   48,	 2,	   35,	 1,	  0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Pandya',   42,	   36,	  3,	3,	   30,	 0,	   25,	 0,	  1,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Jadeja',   18,	   10,	  1,	1,	   60,	 3,    50,	 2,	  1,	 0,	   1);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Kedar',	   65,	   60,	  7,	0,	   24,	 0,	   24,	 0,	  0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Ashwin',   23,	   42,	  3,	0,	   60,	 2,	   45,	 6,   0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Umesh',	   0,	   0,	  0,	0,	   54,	 0,	   50,	 4,	  1,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Bumrah',   0,	   0,	  0,	0,	   60,	 2,	   49,	 1,   0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Bhuvi',	   15,	   12,	  2,	0,	   60,	 1,	   46,	 2,	  0,	 0,	   0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Rohit',	   46,	   65,	  5,	1,	   0,	 0,	   0,	 0,	  1,	 0,    0);''')
cursor.execute('''INSERT INTO MATCH
VALUES('Kartick',  29,	   42,	  3,	0,	   0,	 0,	   0,	 0,	  2,	 0,	   1);''')
Cricket.commit()
cursor.execute('''INSERT INTO MATCH
VALUES('KL Rahul',    58,	   48,    6,	3,	   0,	 0,	   0,	 0,	  1,	 0,	   1);''')

#POPULATING STATS TABLE
cursor.execute('''INSERT INTO STATS
VALUES('Kohli',    189,    8257,    28,    43,    120,    'BAT');''')
cursor.execute('''INSERT INTO STATS
VALUES('Dhawan',   86,	   3589,	10,	   21,	  100,    'BAT');''')
cursor.execute('''INSERT INTO STATS
VALUES('Rohit',    158,    5435,	11,	   31,	  100,	  'BAT');''')
cursor.execute('''INSERT INTO STATS
VALUES('Kedar',	   25,	   565,	    2,	   1,	  85,	  'AR');''')
cursor.execute('''INSERT INTO STATS
VALUES('KL Rahul',   78,	   2573, 	3, 	   19,	  75,	  'BAT');''')
cursor.execute('''INSERT INTO STATS
VALUES('Bhuvi',    67,	   208,	    0,	   0,	  100,	  'BWL');''')
cursor.execute('''INSERT INTO STATS
VALUES('Umesh',    70,	   77,	    0,	   0,	  75,	  'BWL');''')
cursor.execute('''INSERT INTO STATS
VALUES('Bumrah',   16,	   1,	    0,	   0,	  85,	  'BWL');''')
cursor.execute('''INSERT INTO STATS
VALUES('Ashwin',   111,	   675,	    0,	   1,	  90,	  'BWL');''')
cursor.execute('''INSERT INTO STATS
VALUES('Jadeja',   136,	   1914,	0,	   10,	  100,	  'AR');''')
cursor.execute('''INSERT INTO STATS
VALUES('Dhoni',     296,   9496,	10,	   64,	  110,	  'WK');''')
cursor.execute('''INSERT INTO STATS
VALUES('Kartick',   73,	   1365,	0,	   8,	  60,	  'WK');''')
cursor.execute('''INSERT INTO STATS
VALUES('Pandya',	17,	   289,	    0,	   2,	  75,	  'AR');''')
cursor.execute('''INSERT INTO STATS
VALUES('Yuvraj',	304,   8701,	14,	   52,	  85,	  'BAT');''')
cursor.execute('''INSERT INTO STATS
VALUES('Axar',	    11,    111,	    0,	   0,	  75,	  'AR');''')
Cricket.commit()
Cricket.close()

