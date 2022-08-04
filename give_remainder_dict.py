'''READ ME FIRST PLEASE: I have explained every line with the help of comments and I have also used docstring to explain some line with examples and with more detail. Here 'number_of_digits' is the number of digits you want to count after the decimal point 

-Also I have left print statements after each variable so that we can always uncomment them see what are they printing or storing.
'''


#Start of the code


'''Using decimal module to achieve precision in larger decimal values.getcontext() and Decimal()
are the objects of this module.'''

from decimal import getcontext,Decimal   

def give_remainder_dict(dividend,divisor,number_of_digits):   #defining the function using 'def' keyword which has three arguments(dividend,divisor,number_of_digits).

    ''' from here all the comments are written on the case where dividend is the 22 , divisor is 7 and numbers=100. 
            22/7=3.14....
    
    
    
     '''    
    
    integer_part_quotient=dividend//divisor  #calculating the integer part of the quotient which is 3.

    # print(f"integer part is {integer_part_quotient}")

    '''The getcontext(). prec set the precision of digits which Decimal lib will use to return any calculated number.'''
    
    if str(integer_part_quotient)[0]!='0':  #if '3' zero indexed not equal to zero 
        getcontext().prec = number_of_digits+1       #we will add +1 to number_of_digits in the precision of getcontext() because '3' will be included as significant figure and hence we need to add 1 to adjust the correct decimal values # here numbers is the precison of decimal values we need after the decimal point.

    else:
        getcontext().prec = number_of_digits  #we will not add +1 because a leading zero at zero indexed  is not considered a significant figure.

        '''for example in the case of 1/3=0.3333 we have 0 as the zero indexed value of integer part of quotient.'''

        
    
    quotient=Decimal(dividend) / Decimal(divisor)   #calculating the precise value of quotient to the required precision. 
    
    # print(f"quotient is {quotient}")
    
    quotient_after_decimal=str(quotient)[(len(str(integer_part_quotient)))+1: ]  #using string slicing to get only numbers after decimal point.

    # print(f"quotient after decimal is {quotient_after_decimal}")
    
    l=(len(str(quotient_after_decimal)))      #calculating the length of numbers after decimal point
    
    # print(f"length of quotient_after_decimal is {l}")
    
    
    if l==number_of_digits:       #if l is equal to number_of_digits which is 100 then we will go run the code inside if statement. Because in the case where 100 is the dividend and 25 is the divisor there l is not equal to numbers because it completely divides the dividend.

        result={}       #creating a empty dictionary to store the final result
        for i in range(10):   #since we need to count the frequency of 0,1,2,3,4,5,6,7,8,9, we used range(10) here
            j=str(i)          #converting i into string and storing it into j variable.
            result[j]=(quotient_after_decimal.count(j))  #using dictionary methods and count function to store the frequencies of each number.
            
            
        return result    #returning result
    
    else:   #in the case of 100/25 where numbers is 4     #and similar cases
        float_quotient=float(quotient)  #calculating float value of quotient, for example 4 -->4.0
        precision="."+str(number_of_digits)+"f"  #here precision-->.nf  where n is the number_of_digits .

        # print(f"precion is {precision}")
        
        result= (format(float_quotient, precision))  #using format, for example,result=(format(4.0,".4f"))

        # print(f"result is {result}")

        result_after_decimal=str(result)[(len(str(integer_part_quotient)))+1: ]  ##using string slicing to get only numbers after decimal point.

        
        # print(f"result_after_decimal is {result_after_decimal}")
        
        result={}     #doing same as we did in the if statement above
        for i in range(10):
            j=str(i)
            result[j]=(result_after_decimal.count(j))
        return result    
    



if __name__ == "__main__":
    dividend=int(input("Enter the dividend please: "))
    divisor=int(input("Enter the divisor please: "))
    number_of_digits=int(input("Enter number of digits you want to count after the decimal point : "))

    print(give_remainder_dict(dividend,divisor,number_of_digits))