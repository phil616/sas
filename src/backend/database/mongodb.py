import motor.motor_asyncio

async def connect_to_mongodb():
    client = motor.motor_asyncio.AsyncIOMotorClient(('mongodb://admin:123456@192.168.0.3:27017/'))
    db = client['test_database']
    return db


