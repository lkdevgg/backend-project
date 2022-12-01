import motor.motor_asyncio

MONGODB_URL = "mongodb://admin:admin@172.18.140.200:27018"
DATABASE_NAME = "test"

class Database():
    def __init__(self) -> None:
        self.connected = False
        self.mongodb_client = None

    async def db_connection(self):
        if self.connected == False:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
            self.connected = True
        db = self.client[DATABASE_NAME]
        return db


database = Database()
