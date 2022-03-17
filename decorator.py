def capitalize(fun):
    def wrapper():
        res = fun()
        tocapital = res.upper()
        return tocapital
    return wrapper
@capitalize
def capital():
    return 'test'
message = capital()
print(message)