from fastapi import APIRouter, HTTPException
from ..models.user import UserCreate, User
from ..utils.auth import get_password_hash
from fastapi import Request

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, request: Request):
    try:
        # Check if user exists
        existing_user = await request.app.mongodb["users"].find_one({"email": user.email})
        print(f"Existing user check: {existing_user}")  # Debug print
        
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create new user
        user_dict = user.dict()
        user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
        user_dict["is_active"] = True
        
        print(f"User dict before insert: {user_dict}")  # Debug print
        
        # Insert into MongoDB
        result = await request.app.mongodb["users"].insert_one(user_dict)
        
        # Fetch the created user
        created_user = await request.app.mongodb["users"].find_one({"_id": result.inserted_id})
        print(f"Created user from MongoDB: {created_user}")  # Debug print
        
        if not created_user:
            raise HTTPException(status_code=404, detail="User not found after creation")
            
        # Convert MongoDB document to User model
        user_response = User.from_mongo(created_user)
        print(f"Final user response: {user_response}")  # Debug print
        
        return user_response
        
    except Exception as e:
        print(f"Error creating user: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=str(e))