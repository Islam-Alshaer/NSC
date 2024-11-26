"""
Eslam Saeed Hamdy Hassan           20230060
Eslam Waleed Salah AbdElmotaleb    20230062
Youssef Farid Sayed Hassanin       20230504
"""

#this function converts any number to decimal no matter what case it is 
def convert_to_decimal(num, base) :

    
    NUM_SIZE = int(len(num))
    decimal_equivalent = 0
    
    #loop on the string form the end
    for i in range(NUM_SIZE - 1, -1, -1) :
        """
        to convert (125)8 to decimal we take the last digit "5"
        it is between 0 and 9 so we take the integer value of it and multiply it by base(8) to the power (NUM_SIZE (3) - i (2) - 1) = 5 * (8 ** 0) = 5 and so on
        2 * (8 ** 1) + 1 * (8 ** 2) = 5 + 16 + 64 = (85)10 which is indeed the value of the decimal equevalent
        """
        if(ord(num[i]) >= ord('0') and ord(num[i]) <= ord('9')) :
            current_digit_number = int(num[i])
        else :
            current_digit_number = ord(num[i]) - ord('A') + 10

        #multiply by the base to the power of the current digit - 1 and add to a number
        decimal_equivalent += current_digit_number * (base ** (NUM_SIZE - i - 1) )
         
    #return the decimal equivalent
    return decimal_equivalent

def convert_to_wanted_base(N, base):

    N = int(N)
    table = "0123456789ABCDEF"
    FResult = ""

    while N != 0:
        result = N % base
        FResult = table[result] + FResult
        N //= base

    print(FResult)
    



def is_the_right_base(N, base) :
    #transforming the value of numbers base to integer 
    valid = ""
    #if the number is decimal the valid numbers to see are 0123456789 and if binary 0 1 and so on
    if base == 10 :
        valid = "0123456789"
    elif base == 2 :
        valid = "01"
    elif base == 8 :
        valid = "01234567"
    elif base == 16 :
        valid = "0123456789ABCDEF"
    #125 (octa) as an example 
    for ch in N :
        #check if there is a letter in the middle that is not valid
        if(ch not in valid) :
            return False

        #note that : 1 is in the string valid ("01234567") as well as 2 and 5

    #notice that if the function has not stopped till now that means all numbers are valid 
    return True



# all code should be in a loop so that we can iterate as much as user wants in Menu 1
while True :
    print("** numbering system converter ** \nA) insert a new number \nB) Exit program\n")
    query = input()

    #in case of continue the program
    if query == 'A' :
        #we declare needed variables so it is visible in the whole scope
        num = "" 
        numbers_base = ""
        wanted_base = ""
        
        #Menu 2
        while True :
            #taking the number and base of the number
            num = input("Please insert a number: ") 
            #as a test case we take 125 (octa decimal)
            print("** Please select the base you want to convert a number from**\n")
            print("A) Decimal\nB) Binary\nC) octal\nD) hexadecimal")
            numbers_base = input()

            #convert the numbers base to the integer value actaully meaned
            if numbers_base == 'A' :
                numbers_base = 10
            elif numbers_base == 'B' :
                numbers_base = 2
            elif numbers_base == 'C' :
                numbers_base = 8
            elif numbers_base == 'D' :
                numbers_base = 16
            #in case of invalid input
            else :
                print("Please select a valid choice\n")
                continue
            
            #125 is octa decimal number (look into the note in the function above)
            if not is_the_right_base(num, numbers_base) :
                print(num, "is not a valid number in base ", numbers_base)
                continue
            break

        #Menu 3
        while True : 
            #taking the base user wants to convert to 
            print("** Please select the base you want to convert a number to**")
            print("A) Decimal\nB) Binary\nC) octal\nD) hexadecimal")
            wanted_base = input()
    
            #in case of invalid input
            if(ord(wanted_base) < 65 or ord(wanted_base) > 68) :
                print("Please select a valid choice")
            else :
                break


        #transfering the wanted_base to a number instead of a letter
        if wanted_base == 'A' :
            wanted_base = 10
        elif wanted_base == 'B' :
            wanted_base = 2
        elif wanted_base == 'C' :
            wanted_base = 8
        elif wanted_base == 'D' :
            wanted_base = 16
        
        
        
        #processing

        #since it does not make any sense to convert a number to the same base
        if numbers_base == wanted_base :
            print(num)
            break
        else :
            #convert any h based number to decimal but handeling the case of decimal since converting is useless in that case
            if numbers_base != 'A' :
                # to convert (125)8  to decimal we use function "convert_to_decimal"
                num = str(convert_to_decimal(num, numbers_base))
            
            if wanted_base != 'A'  :     
                #convert the decimal value to the wanted base 
                convert_to_wanted_base(num, wanted_base)  
                
            else :
                print(num)
            
    #in case fo quitting the program
    elif query == 'B' :
        break

    #in case of invalid input
    else :
        print("please select a valid choice")
        continue