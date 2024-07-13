# json_asynchronous_nosql_encrypted_database
from asyncio import run
from re import findall
from datetime import datetime
from os.path import exists
from os import getpid, kill, environ
from signal import SIGTERM
from json import loads
from cryptography.fernet import Fernet

p = print

class Safe:
    def __init__(self) -> None:
        self.safe_key = environ.get("safe_key", False)
        if not self.safe_key:
            exit("Safe key not found in the environment!")

    async def tool(self, og):
        try:
            if isinstance(og, (list)):
                data = Fernet(self.safe_key.encode()).encrypt(str(og[0]).encode("utf-8")).decode('utf-8')
            elif isinstance(og, (tuple)):
                data = Fernet(self.safe_key.encode()).decrypt(str(og[0]).encode("utf-8")).decode('utf-8')
            else:
                return
            return data
        except Exception as e:
            p(e)

safe = Safe()

class Regulate:
    def __init__(app, e=None, do=None) -> None:
        app.process = getpid()
        app.e = e
        if not do:
            app.kill()
        
    def kill(app):
        if app.e:
            app.e = str(app.e).strip()
            p(f'Terminating Service {app.process}...Errors>> {app.e} <<..')

        kill(app.process, SIGTERM)

    async def log(app):
        app.e = str(app.e).strip()
        if "KeyboardInterrupt" in app.e:
            app.kill()

        p(app.e)
        return app.e

class Db:
    def __init__(app, name: str=None) -> None:
        app.save_data = [None, "y"][0]
        if not name:
            app.db = "db.anonyx"
        else:
            app.db = name

        if not exists(app.db):
            return

        app.instance = None

    async def protect(app, data, state: str="encrypt"):
        for k, v in data.items():
            if not isinstance(v, (list, tuple, dict)):
                if state == "encrypt": action = [v,]
                else: action = (v,)

                value = await safe.tool(action)
                if value:
                    data.update({k: value})

            elif isinstance(v, (dict)):
                for k2, v2 in v.items():
                    if not isinstance(v2, (list, tuple, dict)):
                        if state == "encrypt": action = [v2,]
                        else: action = (v2,)

                        value = await safe.tool(action)
                        if value:
                            data[k].update({k2: value})

            elif isinstance(v, (list)):
                for index, item in enumerate(v):
                    if not isinstance(item, (list, tuple, dict)):
                        if state == "encrypt": action = [item,]
                        else: action = (item,)

                        value = await safe.tool(action)
                        if value:
                            data[k][index] = value
        return data

    async def write(app, data):
        try:
            data = await app.protect(data)
            with open(app.db, "a", encoding="utf-8") as f:
                f.write("record == time_stamp: {}, data: {} ==".format( str( datetime.now() ), str(data) ) + "\n")

        except Exception as e:
            p(f"Something went wrong while writing to db... {e}")

    async def read(app, chunk_size: str = 1024):
        try:
            with open(app.db, "r", encoding="utf-8") as f:
                content = ""
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        yield None
                        return
                    else:
                        content += chunk
                    
                    items = findall(r"record == (.*?) ==", content)

                    if items != []:
                        for item in items:
                            if item != []:
                                item = findall(r", data: (.*?)$", item)

                                if item != []:
                                    item = item[0]
                                    item = item.replace("'", '"')
                                    item = loads(item)
                                    yield await app.protect(item, 'decrypt')

                        for i in items:
                            content = content.replace(i, "")

        except Exception as e:
            p(f"Something went wrong while reading db... {e}")
            yield 'Something went wrong'
            return

# Example
class App:
    def __init__(app) -> None:
        app.db = Db()

    async def __main__(app):
        try:
            data = {
                'name': 'test',
                'dict': {'name': 'example'},
                'list': ['example'],
            }

            # Query for a record from the db using it's name
            async for item in app.db.read():
                if item:
                    if item.get("name", None) == data["name"]:
                        p(item)
                        break
                    else:
                        item = None

            # Create and save record to db
            if not item:
                p("Record not found in the database...")
                await app.db.write(data)

        except KeyboardInterrupt:
            Regulate()
        except Exception as e:
            Regulate(e)

if __name__ == '__main__':
    try:
        run(App().__main__())
    except KeyboardInterrupt: pass
