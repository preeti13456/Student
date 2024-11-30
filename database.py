from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DB_URL = "mongodb+srv://preetidevsang:<db_password>@cluster0.oqtgk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_DB_URL)
db = client.student_management  # Database name
