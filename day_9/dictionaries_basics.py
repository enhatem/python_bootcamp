#Dictionary syntax : {key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retreiving items from dictionary.
#print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary
empty_dictionaty={}

#Wipe an existing dictionary (useful when we want to clear out a user's progress or if a game restarts)
# programming_dictionary={}
# print(programming_dictionary)

#Edit an item in a dictionaty
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log)

#Nesting Dictionary in a list
travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris","Lille","Dijon"], 
    "total_visits": 12
    },
    {
    "country":"Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
    },
]

dic = {}
dic["majestic"] = "yes"
dic[1] = 4
print(dic)


