import sqlite3

from functools import wraps


class Database():
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS prompts (body, collection)")
        self.conn.close()

    def db_handler(func):
        """
        Note: @wraps is mandatory for docstrings to work on wrapped functions.
        We must return result, for func(), else the function will be returned
        instead of the values it returns.
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

            result = func(self, *args, **kwargs)
            
            self.conn.close()
            return result

        return wrapper

    @db_handler
    def get_prompts_list(self):
        response = self.cursor.execute("select *, rowid from prompts")
        return response.fetchall()

    @db_handler
    def create_prompt(self, prompt):
        #TODO: implement duplicate spotting
        self.cursor.execute("""INSERT INTO prompts(body, collection)
                            VALUES(?, 'null')""", (prompt,))
        self.conn.commit()

    @db_handler
    def create_prompt_list(self, prompts):
        #TODO: implement duplicate spotting
        prompts = [(pr,) for pr in prompts]
        self.cursor.executemany("""INSERT INTO prompts(body, collection)
                            VALUES(?, 'null')""", prompts)
        self.conn.commit()

    @db_handler
    def delete_prompt(self, prompt_id):
        print("aaa")
        self.cursor.execute("""DELETE FROM prompts WHERE
                            rowid = ?""", (str(prompt_id),))
        self.conn.commit()

    @db_handler
    def edit_prompt_body(self, prompt, new_prompt):
        self.cursor.execute("""UPDATE prompts
                            SET body = ?
                            WHERE body = ?""", (new_prompt, prompt))
        self.conn.commit()

    @db_handler
    def edit_prompt_collection(self, prompt, new_collection):
        self.cursor.execute("""UPDATE prompts
                            SET collection = ?
                            WHERE body = ?""", (new_collection, prompt))
        self.conn.commit()