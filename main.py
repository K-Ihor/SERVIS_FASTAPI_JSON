import re
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI() # экземпрляр app



# @app.get("/")
# def index_page(): 
#     with open('page.html', 'r') as f:
#         page = f.read()
#         return Response(page, media_type="text/html")

def standardization_phone_number(num1: str) -> str:
    result = re.findall(r'\d', num1)
    if 10 <= len(result) <= 11:
        if len(result) == 10:
            if result[0] == "9": # and result[1] == "1" and result[2] == "2":
                return f"8 ({''.join(result[0:3])}) {''.join(result[3:6])}-{''.join(result[6:8])}-{''.join(result[8:10])}"
            else:
                return''.join(result)
        elif len(result) == 11: 
            if result[0] == "7" or result[0] == "8":
                result[0] = "8 "
                return f"{result[0]}({''.join(result[1:4])}) {''.join(result[4:7])}-{''.join(result[7:9])}-{''.join(result[9:11])}"
            else:
                return ''.join(result)
        else:
            return ''.join(result)
    else:
        return ''.join(result)






# def standardization_phone_number(num1: str) -> str:
#     num = "".join(filter(str.isdigit, num1))
#     if len(num) < 10 or len(num) > 11 or num[-10] != '9':
#         print(num)
#     phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
#     # print(phone)
#     return phone


@app.post("/unify_phone_from_json")
def process_page(data: dict = Body(...)):
    input_phone = data["userphone"]
    response = standardization_phone_number(input_phone)      
    # response = Response(
    #     json.dumps({
    #         "success": True,
    #         "message": f"Привет! Ваш номер<br />{input_phone}"
    #     }),
    #      media_type='application/json')
    #return response
    return HTMLResponse(content=response, status_code=200)


