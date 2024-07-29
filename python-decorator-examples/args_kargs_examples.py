def testing(*args,**kwargs):
    print(f"Args = {args}")
    print(f"KWargs = {kwargs}")

# Args = ('hello', 1)
# KWargs = {'name': 'shekhar'}
testing("hello",1,name="shekhar")