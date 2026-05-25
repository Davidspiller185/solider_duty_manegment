from data import lst_solder
def find_solider_by_id(solider_id:int) ->dict |None:#מחפשת חייל לפי id ומחזירה אותו
    lst=lst_solder()
    for dic in lst:
        if dic["id"]==solider_id:
            return dic
    return None

def is_valid_status(status:str) ->bool:# בדיקה אם הסטטוס חוקי
    lst_status=["pending","completed","missed"]
    if status not in lst_status:
        return False
    return True

def is_valid_name(name:str) ->bool:#בדיקה אם השם תקין שהוא לא ריק
    if name:
        return True
    return False

def solider_has_duty(solider:dict,duty_name:str) ->bool:#בדיקה אם לחייל יש כבר את אותה תורנות עם השם המסויים
    for dic in solider["duties"]:
        if dic["name"]==duty_name:
            return True
    return False

def is_valid_day(dat:str) ->bool:#בדיקה אם היום הוא חוקי שהוא לא יום שישי או שבת 
    lst_days=["sunday","monday","tuesday","wednesday","thursday"]
    lst_not_valid=["friday","saturday"]
    if dat not in lst_days or dat in lst_not_valid:
        return False
    return True
    

