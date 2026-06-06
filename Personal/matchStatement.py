class Point : 

    __match_args__ = ("x","y")
    x: int
    y: int
def where_is(point):
    match point: 
        case Point(x,y):
            print(f"{x},{y}")
        case 400:
            print("400")
        case 4005:
            print("4005")
        case "raymu":
            print("raymu")
        case [0,3,4]:
            print("[0,3,4]")
        case _: 
            print("Not a point")

where_is(400)
where_is(4005)
where_is("raymu")
where_is([0,3,4])
where_is((0,0))