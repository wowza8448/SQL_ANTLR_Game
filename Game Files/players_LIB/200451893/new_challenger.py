import random
import math

num = 1
new_num = 0
new_x = 0
new_y = 0
player_count = 0
counter = 0
second_counter = 0
def init():
    return("🐰")


def run(db_cursor , state):
    global num
    global new_num
    global new_x
    global new_y
    global counter
    global second_counter
    rows = db_cursor.execute(f"select * from main_game_field as gf, owner where is_flag = 0 and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    global player_count
    player_count = 0
    
    for row in rows.fetchall():
        player_count = player_count + 1
        if player_count == 1:
            if counter == 0:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] - 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 1:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 2:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 3:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 4:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                counter = counter + 1
            elif counter == 5:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                counter = counter + 1
            elif counter == 6:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                counter = counter + 1
            elif counter == 7:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 8:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1  }, 'MOVE')")
                counter = counter + 1
            elif counter == 9:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1 }, 'MOVE')")
                counter = counter + 1
            elif counter == 10:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                counter = counter + 1
            elif counter == 11:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                counter = counter + 1
            elif counter == 12:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                counter = 1
        elif player_count == 2:
            if second_counter == 0:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] - 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 1:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 2:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 3:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] + 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 4:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 5:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 6:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 7:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 8:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1  }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 9:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 0 }, {row[1] - 1 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 10:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 11:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = second_counter + 1
            elif second_counter == 12:
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 0 }, 'MOVE')")
                second_counter = 0
        else:
            if (num == 1):
                test = db_cursor.execute(f"select * from main_game_field as gf, owner where owner.name != '{state['NAME']}' and is_flag = TRUE ORDER BY x ASC")
                new_row = test.fetchone()
                if (new_row[5] != 'players.200451893.new_challenger'):
                    new_x = new_row[0]
                    new_y = new_row[1]
                    num = num + 1
            if (new_num == 3):
                test = db_cursor.execute(f"select * from main_game_field as gf, owner  where is_flag = TRUE and gf.owner_id != owner.owner_id ORDER BY x DESC")
                new_row = test.fetchone()
                new_x = new_row[0]
                new_y = new_row[1]
                new_num = new_num + 1
            
            if (row[0] == new_x and row[1] == new_y):
                new_num = new_num + 1
            if (row[0] > new_x and row[1] > new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] - 1 }, 'MOVE')")
            elif (row[0] > new_x and row[1] < new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 1 }, 'MOVE')")
            elif (row[0] < new_x and row[1] > new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] + 1 }, {row[1] - 1 }, 'MOVE')")
            elif (row[0] < new_x and row[1] < new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] + 1 }, { row[1] + 1  }, 'MOVE')")
            elif (row[0] == new_x and row[1] < new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] }, { row[1] + 1  }, 'MOVE')")
            elif (row[0] == new_x and row[1] > new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] }, { row[1] - 1  }, 'MOVE')")
            elif (row[0] < new_x and row[1] == new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] + 1 }, { row[1] }, 'MOVE')")
            elif (row[0] > new_x and row[1] == new_y and row[5] == 'players.200451893.new_challenger'):
                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, { row[0] - 1 }, { row[1] }, 'MOVE')")