def do_stuff(num):
    '''This is a simple function we are using to practice creating Unit Tests in another file'''
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        print("There has been a ValueError here good sir!")
        return err          
        #using raise here seems to result in an error when trying to run the test (ValueError)  I am not exactly sure why