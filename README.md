The **json_asynchronous_nosql_encrypted_database** library provides a secure, asynchronous NoSQL database solution for Python applications. It integrates encryption and decryption functionalities to safeguard data integrity, ensuring sensitive information remains protected. Built with asyncio for efficient concurrent operations, it supports seamless data storage and retrieval using JSON format, offering flexibility and performance in data management.

**Features:**
- **Asynchronous Operation:** Built with asyncio, enabling concurrent operations for efficient data handling.
- **Encryption:** Utilizes Fernet encryption to secure data at rest, protecting against unauthorized access.
- **Data Protection:** Supports encryption of JSON data structures, ensuring sensitive information remains confidential.
- **Simple Integration:** Easy-to-use interface for writing and reading encrypted data to/from the database.
- **Error Handling:** Provides robust error handling capabilities for smooth operation.

**Installation:**
```bash
pip install git+https://github.com/anonyxbiz/janed
```

**Usage Example:**
```python
from asyncio import run
from janed import Db

class App:
    def __init__(app) -> None:
        app.db = Db("my.db")

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
                        print(item)
                        break
                    else:
                        item = None

            # Create and save record to db
            if not item:
                print("Record not found in the database...")
                await app.db.write(data)

        except Exception as e:
            print(e)

run(App().__main__())

```

**Contributing:**
Contributions, issues, and feature requests are welcome!.

**License:**
This project is licensed under the MIT License - see the [LICENSE] file for details.
