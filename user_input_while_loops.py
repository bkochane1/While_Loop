num_of_employees = 0 # keep track how many times you went through loop
employees = [] # hold all the emplyee records

while num_of_employees < 5: # Only accept five employee records

    while True:
        employee_id = input("Please enter an employee ID: ") # set employee id as input

        try: # if there is an error( employee id is 7 or less digit long) inside the try then go to the except
            int(employee_id)
            if len(employee_id) > 7:
                print("Re enter")
                continue # If too long continue loop
            break # Exit loop
        except:
            print("Re enter")
            continue # If information enter incorrectly continue loop

    invalid_characters_name = ["!", '"', "@", "#",'$','%','^', '&', '*',"(", ")","_",'+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\'] # name cannot contain these characters

    while True:
        employee_name = input("Please enter an employee name: ") 

        for letter in employee_name: # loop through all the letters in the employees name 
            for invalid_char in invalid_characters_name:
                if letter == invalid_char: # if the letters in the employees names match any invalid then continue
                    print("Re enter")
                    continue
        break

    invalid_characters_email = ["!", '"', "'", "#",'$','%','^', '&', '*',"(", ")", '+','=',',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']

    while True:
        employee_email = input("Please enter an employee email: ")

        for letter in employee_email: # loop through all the letters in the employee email
            for invalid_char in invalid_characters_email:
                if letter == invalid_char: #if the letters in the employees names match any invalid then continue
                    print("Re enter")
                    continue
        break

    invalid_characters_address = ["!", '"', "'", "@", '$','%','^', '&', '*',"_",'+','=', '<', '>', '?', ';', ':', '[', ']', '{', '}', '\\'] # invalid characters in address

    while True:
        employee_address = input("Please enter an employee address: ") 

        for letter in employee_address: # loop through all the letters in the employee address
            for invalid_char in invalid_characters_address:
                if letter == invalid_char: ##if the letters in the employees names match any invalid then continue
                    print("Re enter")
                    continue
        break

    print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". ")

    if len(employee_address) == 0: # if employees don't provides address print message
        print("You did not provide an address.")
        employees.append({'employee_name': employee_name, 'employee_id': employee_id, 'employee_email': employee_email}) # add employee dict record
    else:
        print("Your address is " + employee_address) # if employee provides address print message
        employees.append({'employee_name': employee_name, 'employee_id': employee_id, 'employee_email': employee_email, 'employee_address': employee_address}) # add employee dict record that includes an address

    num_of_employees = num_of_employees + 1 # Keep track of the number of employees added

print(employees) # print final results after end of while loop