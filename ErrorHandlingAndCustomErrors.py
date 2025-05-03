from CustomExcception import CustomException

def handleExceptions(n:int):
    try:
        print(8/n)
        print("hello" + "L")
        int("abc")
    
    except ZeroDivisionError:
        print("got ZeroDivisionError")
    except TypeError:
        print("got TypeError")
    except ValueError:
        print("got ValueError")
    except Exception:
        print("Got some diff exception")

def ageException(age : int):
    if age < 18:
        raise CustomException("You are not old enough to be drinking")
    
def useFinally(n):
    try:
        print("string" + n)
    except Exception:
        print("Exception")
    finally:
        print("I'm still in Finally")

if __name__=="__main__":
    handleExceptions(8)
    useFinally(78)
    ageException(9)