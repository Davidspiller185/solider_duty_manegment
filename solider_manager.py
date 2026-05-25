from data import dic_solder,lst_solder
from utils import find_solider_by_id
def add_solider(solider_id:int,name:str)->None:#מוסיפה חייל חדש למערכת
    dic_solider=dic_solder()
    dic_solider["id"]=solider_id
    dic_solider["name"]=name
    lst=lst_solder()
    lst.append(dic_solider)
    

def remove_solider(solider_id:int)->None:#מסירה חייל מהמערכת לפי id
    lst=lst_solder()
    result=find_solider_by_id(solider_id)
    if result is not None:
        lst.remove(result)
    else:
        raise KeyError("the solider id not defined")
    

def get_all_solider()->list:# מחזירה את רשימת כל החיילים במערכת
    lst=lst_solder()
    return lst



