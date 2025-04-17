# Global Scopes
enemies = 1 # Global variable

def local_value_enemies():
    enemies = 2 # In local function
    print(f"enemies inside function: {enemies}")

local_value_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def local_value_health():
    health = 3
    print(f"value inside health: {health}")

local_value_health()
# print(f"value outside health: {health}") # Error - because variable is not global