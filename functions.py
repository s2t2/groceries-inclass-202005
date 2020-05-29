# custom-functions/my_functions.py

def celsius_to_fahrenheit(celsius_temp):
    #print(celsius_temp)
    #return 9/5 * celsius_temp + 32
    f_temp = 9/5 * celsius_temp + 32
    return f_temp

def numeric_to_letter_grade(n):
    if n < 60:
        return "F"
    elif n < 70:
        return "D"
    elif n < 80:
        return "C"
    elif n < 90:
        return "B"
    else:
        return "A"

# prefer to pass in y as a parameter if our function needs it
#def other_func(x):
#    return x + y

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = input("Please input a numeric letter grade (from 0 to 100): ") # 87.5
    print(type(score)) #> str
    score = float(score)
    # todo: ensure the provided input value is valid before passing it in to the function below:
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)

    ## lesson: if your functions needs a variable, pass in that variable as a parameter
    #print(other_func(6) #> error
    #y = 5
    #print(other_func(6) #> works by coincidence
