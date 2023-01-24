def function (x):
    while(True):
        x+=512
        yield(x)

startingPoint=int(input("Enter a starting number between 0 and 511: "))
if (startingPoint<0 or startingPoint>511):
    print("Number out of range, exiting program.")
    exit()
else:
    print(startingPoint)
generator_object = function(startingPoint)
while True:
    print(next(generator_object))
