#Seatwork 1, Q2
from pyscript import document, display 


def student_checker(e):

    document.getElementById('results').innerHTML = "" #clear

    #list of students
    names_of_students = ['Girlie Jackstone', 'Mark Jackstone', 'Peter Jackstone', 'Panying Jackstone'] 

    #get the values
    firstName = document.getElementById('FirstName').value
    lastName = document.getElementById('LastName').value

    #combine
    name = firstName + " " + lastName

    #checks if the name is on the list
    is_name = name in names_of_students 

    messages = {
        True: f"Congratulations {name}, you are now a member of the Social Sciences club!",
        False: f"Sorry {name}, you are not a member of the Social Sciences club!"
    }

    display(messages[is_name], target="output")






    
