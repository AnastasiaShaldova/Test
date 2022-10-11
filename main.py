from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

from app.captcha import captcha

app = FastAPI()

#
# @app.post("/users")
# async def save_user(user_details: User):
#     return {'name': user_details.user_name, 'gender': user_details.gender}
#
#
# @app.get("/users/users_get")
# async def users_list():
#     return await users_get()
#
#
# @app.get("/users/user_get_name")
# async def user_get_name(user_details: str):
#     return get_user_by_name(user_details)


@app.get('/GetCaptchaImg')
async def _get_captcha_img(request: Request):
    data, get_uuid = captcha.get_img()
    headers = {'get_uuid': get_uuid}
    return StreamingResponse(data, media_type='image/jpeg', headers=headers)

@app.get('/CheckCaptcha')
async def _get_captcha_text(request: Request):
    if captcha.is_captcha_valid(request.headers.get('text', ''), request.headers.get('get_uuid', '')):
        return JSONResponse(content='OK', status_code=200)
    return JSONResponse(content='Error', status_code=200)


