from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from app.config import get_settings
import time

async def test_connection():
    settings = get_settings()
    client = None
    
    print("\n=== Database Connection Test ===")
    
    try:
        print("1. Attempting to connect to MongoDB...")
        client = AsyncIOMotorClient(settings.mongodb_url)
        
        # Test 1: Ping database
        print("2. Testing ping...")
        start_time = time.time()
        await client.admin.command('ping')
        ping_time = time.time() - start_time
        print(f"   ✓ Ping successful! (Latency: {ping_time:.3f}s)")
        
        # Test 2: Database access
        print("3. Testing database access...")
        db = client[settings.database_name]
        
        # Test 3: Write operation
        print("4. Testing write operation...")
        result = await db.users.insert_one({"test": "data"})
        print("   ✓ Write operation successful!")
        
        # Test 4: Read operation
        print("5. Testing read operation...")
        doc = await db.users.find_one({"test": "data"})
        if doc:
            print("   ✓ Read operation successful!")
        
        # Test 5: Clean up
        print("6. Cleaning up test data...")
        await db.users.delete_one({"test": "data"})
        print("   ✓ Cleanup successful!")
        
        print("\n✅ All database tests passed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during database testing: {str(e)}")
    finally:
        if client:
            print("\n7. Closing database connection...")
            client.close()
            print("   ✓ Connection closed")
        print("\n=== Database Test Complete ===\n")

if __name__ == "__main__":
    asyncio.run(test_connection()) 