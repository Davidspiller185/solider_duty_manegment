from data import dic_shifts
from utils import find_solider_by_id,is_valid_status,is_valid_name,solider_has_duty,is_valid_day
def add_duty_to_solider(solider_id:int,duty_name:str,day:str)->None:#מוסיף תורנות חדשה לחייל
    day=day.lower()
    duty_name=duty_name.lower()
    result=find_solider_by_id(solider_id)
    if result is None:
        raise KeyError("the solider id not find")
    if not is_valid_name(duty_name):
        raise ValueError("the name is illegal because is empty") 
    if solider_has_duty(result,duty_name):
        raise ValueError("the solider have already this duty")
    if not is_valid_day(day):
        raise ValueError("the day is  illegal")
    dic_duty=dic_shifts()
    dic_duty["name"]=duty_name
    dic_duty["day"]=day
    dic_duty["status"]="pending"
    result["duties"].append(dic_duty)

def update_duty_status(solider_id:int,duty_name:str,new_status:str)->None:#מעדכנת סטטוס תורנות
    new_status=new_status.lower()
    result=find_solider_by_id(solider_id)
    if result is None:
        raise KeyError("the solider id not find")
    flag=False
    for dic in result["duties"]:
        if dic["name"]==duty_name:
            flag=True
    if not flag:
        raise KeyError("not find a duty with this name for this solider")
    if not is_valid_status(new_status):
        raise ValueError("the new status is illegal")
    
    
    


def get_solider_duties(solider_id:int)->list:#מחזיר רשימת תורנויות של חייל
    result=find_solider_by_id(solider_id)
    if result is None:
        raise KeyError("the solider id not find")
    return result["duties"]

