from fastapi import APIRouter
from model.GPA import GPA,GPASchema
gpa_router = APIRouter(prefix="/gpa")

@gpa_router.get("/get/user/scorelist")
async def curd_get_user_score_list(username:str):
    all_result = await GPA.filter(username=username).all()
    return all_result

@gpa_router.post("/new/user/score")
async def curd_post_new_user_score_item(score:GPASchema):
    await GPA.create(**score.model_dump())

@gpa_router.post("/update/user/score")
async def curd_update_user_score_item(score:GPASchema):
    user_score = await GPA.filter(username=score.username).first()
    user_score.update_from_dict(score.model_dump())
    await  user_score.save()

@gpa_router.get("/delete/user/score")
async def curd_delete_user_score_item(gid:int):
    user_score = await GPA.filter(gpa_id=gid).first()
    await user_score.delete()

