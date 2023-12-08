from app_utils.master_imports import *

from app_utils.utils import auth_user_request, getUserDetails
from controller_model import user_accountModel
from fastapi import Form


router = APIRouter()


@router.post("/edit_profile", summary="edit user profile", tags=["User Account"])
def editProfile(profile_details: schema_model.User_EditProfile, db: Session = Depends(get_db), request=Depends(auth_user_request)):
  unique_id = getUserDetails(request['sub'], "unique_id", db)
  if (unique_id == profile_details.unique_id):
      return user_accountModel.editProfileModel(profile_details, db)
  else:
    return{"message":"Invalid user made this request"}
  
 
@router.delete("/delete_user/{unique_id}", summary="delete user", tags=["User Account"])
def delete_user(unique_id, db: Session = Depends(get_db), request=Depends(auth_user_request)):
  user_unique_id = getUserDetails(request['sub'], "unique_id", db)
  if (str(unique_id) == str(user_unique_id)):
   return user_accountModel.delete_user(unique_id, db)
  else:
     return {"message": "Invalid user made this request"}



@router.post("/deactivate_account", summary="deactivate student account", tags=["User Account"])
def editProfile(user_unique_id: int, db: Session = Depends(get_db), request=Depends(auth_user_request)):
    unique_id = getUserDetails(request['sub'], "unique_id", db)
    if (str(unique_id) == (user_unique_id)):
        return user_accountModel.deactivate_accountModel(unique_id, db)
    else:
        return {"message": "Invalid user made this request"}

    

@router.get("/get_user_details", summary="get user details", tags=["User Account"])
def profileDetails(db: Session = Depends(get_db), request=Depends(auth_user_request)):
    unique_id = getUserDetails(request['sub'], "unique_id", db)
    return user_accountModel.profileDetails(unique_id, db)

