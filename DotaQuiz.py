# player_level = 0;

# lvl1 = ["Team Secret", "Team Spirit", "OG", "PSG.LGD"] #first questions
# lvl2 = ["Miposhka", "Mira", "Collapse", "TORONTOTOKYO", "Yatoro"] #second questions
# lvl3 = ["Dark Willow", "Lion", "Phantom Assasin", "Magnus"] #third questions
# lvl4 = ["1", "2", "3", "5", "All heroes"] #fourt questions
# lvl5 = ["Yes", "No"] #fifth questions

# question = [lvl1, lvl2, lvl3, lvl4, lvl5]

# print("Hello, this is TI10 quiz")
# def lvl_system



import sqlite3
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    lvl1 = """ INSERT INTO expenses (id, name) VALUES (1, "TI10 winner is?") """
    lvl2 = """ INSERT INTO expenses (id, name) VALUES (2, "Team Spirit MVP is?") """
    lvl3 = """ INSERT INTO expenses (id, name) VALUES (3, "Hero, which won all games is?") """
    lvl4 = """ INSERT INTO expenses (id, name) VALUES (4, "How many heroes were taken out under the fountain?") """
    lvl5 = """ INSERT INTO expenses (id, name) VALUES (5, "Is that was ez?") """


    cursor.execute(lvl1)
    cursor.execute(lvl2)
    cursor.execute(lvl3)
    cursor.execute(lvl4)
    cursor.execute(lvl5)