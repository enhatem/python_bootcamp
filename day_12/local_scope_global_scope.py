################### Scope ####################

# enemies = 1
#
# def increase_enemies():
#   # NB: Avoid modifying global variable within a location scope (within a function)
#   global enemies  # explicitly saying that we have a global variable named "enemies" outside the function (not recommended)
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)
#
# drink_potion()

# # Global Scope
# player_health = 10
# def drink_potion():
#   potion_strength = 2
#   print(player_health)
#
# drink_potion()
# print(player_health)

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@enhatem"

