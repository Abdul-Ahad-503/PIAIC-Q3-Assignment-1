from fastapi import FastAPI 
import uvicorn

app = FastAPI()

@app.get("/")
def homepage():
    print("Home page")
    return {"message": "Hello, world!"}

student = [
    {
        "ID": 1,
        "name": "John Doe",
        "age": 25,
        "grade": "A",

    }
]

@app.get("/students")
def get_students():
    print("Here are all students")
    return student

@app.get( "/students/{id}")
def  get_one_student(id: int):
    for s in student:
        if s["ID"] == id:
            return s
    return {"error":"Student not found"}

@app.post("/addStudent")
def add_student(iD:int,nme:str,age:int,grd:str):
    print("Adding a new student")
    global student
    student.append( {"ID": iD,"name": nme,"age": age,"grade": grd})
    return {"message" :f"New Student ID:{iD} has been added."}


@app.put("/updateStudent/{iD}")
def update_student(iD:int,nme:str,age:int,grd:str):
    print("Updating student")
    global student
    for s in student:
        if student["ID"] == iD:
            s["name"] = nme
            s["age"] = age
            s["grade"] = grd
            return {"message": f"Student with ID {iD} has been updated."}
    

    return {"message": f"Student with ID {iD} not found."}


@app.delete( "/removeStudent/{iD}")
def remove_student(iD:int):
    print("Removing the selected student")
    global student
    remStudent=None
    for s in student:
        if s["ID"]==iD:
            remStudent=s
    if remStudent is None:
        return{"message":"Student not found."}
    else:
        student.remove(remStudent)
        return{"message":"Student has been deleted","data":remStudent} 

def start():
    uvicorn.run("restapi.main:app", host="localhost", port=8080,reload =True)
