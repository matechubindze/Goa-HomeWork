def outer():
    def inner():
        print("Inner function called")
    inner()

outer()
