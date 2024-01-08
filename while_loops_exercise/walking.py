purpose = 10000 # Target
total_steps = 0 # All steps

while purpose > total_steps: # Цикъла проверява дали Target > All steps
    command = input() # Tук е новата променлива която е от тип стринг
    if command == "Going home": # Тук с тази проверка проверяваме дали "Променливата command" е еднаква на Going home
        steps = int(input()) # Това е нова променлива от тип INT
        total_steps += steps # Тук събираме steps + total_steps = total_steps
        break # Тук спираме с проверката ако променливата command = "Going home"
    current_steps = int(command) # Правим нова проверка която е равна INT-Цяло число от променливата command тоест ако command = integer => command = current_steps
    total_steps += current_steps # Тук събираме current_steps + total_steps = total_steps но това е ако променливата command != "Going home"

difference = abs(total_steps - purpose) # Тук правим нова променлива difference = абсолютната стойност от (total_steps - purpose) тоест ако се получи отрицателно число то автоматично ще бъде сменено в положително
if total_steps >= purpose: # Ако All steps >= purpose да влезем в проверката 
    print("Goal reached! Good job!") # и да принтираме изречението "Goal reached! Good job!" 
    print(f"{difference} steps over the goal!") # и принтитраме f-стринг изречението с променливата difference 
else: # или друго
    print(f"{difference} more steps to reach goal.") # и принтитраме f-стринг изречението с променливата difference
