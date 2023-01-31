def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "first_name":'Tyler', "last_name": "Bifolchi", 
        "student_number": 10275176,
        "pizza_toppings":["mushrooms","olives","bacon"],
        "movies": [{'genre':'action','name':'Fight Club'}, {'genre':'comedy','name':'South Park: Bigger Longer and Uncut'}]
    }

    # TODO: Step 3 - Add another movie to the data structure

    new_movie = {
        'genre':'animation','name':'Shrek 2'
    }


    about_me['movies'].append(new_movie)
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
    return


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    fullname = about_me['first_name']
    lastname = about_me['last_name']
    nickname = about_me['first_name']
    myID = about_me['student_number']
    print(f'My name is {fullname} {lastname}, but you can call me Sir {nickname}')
    print(f'My student ID is {myID}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings'].append(toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("\nMy favorite pizza toppings are: ")
    about_me['pizza_toppings'].sort()
    for i,p in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = p.upper()
        print(f'-{p}')
    add_pizza_toppings(about_me,'CHEESE')
    print("\nMy favorite pizza toppings are: ")
    for p in about_me['pizza_toppings']:
        print(f'-{p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(movie_genres):
    print(f"\nI like to watch ",end='')
    for i, genre in enumerate(movie_genres['movies']):
        if i < len(movie_genres['movies']) - 1:
            print(genre['genre'],end=', ')
        else:
            print("and",end=" ")
            print(genre['genre'],end='.')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print("\nSome of my favorite movies are ",end="")
    for i, name in enumerate(movie_list['movies']):
        if i < len(movie_list['movies']) - 1:
            print(name['name'],end=', ')
        else:
            print("and", end=" ")
            print(name['name'],end=".")
    return
    
if __name__ == '__main__':
    main()