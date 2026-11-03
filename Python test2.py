#Python test2.py
#GitHub-V1.0
print("Welcome to the 2nd Python test file!")
FirstTest = input("Have you completed the first test file (PythonTest.py)? (Y/N): ").strip().upper()
if FirstTest == "Y":
    print("Great! Let's start second test.")
elif FirstTest == "N":
    print("Please complete the first test file (PythonTest.py) before starting this one.")
    ExitChoice = input('Press "E" to exit the code.').strip().upper()
    if ExitChoice == "E":
        exit()
    else:
        print('Invalid input, you will now have to manually close the code. Type "exit()" in the terminal to exit the code.')
else:
    print("Invalid input, please enter Y or N.")
    ExitChoice = input('Press "E" to exit the code.').strip().upper()
    if ExitChoice == "E":
            exit()
    else:
            print('Invalid input, you will now have to manually close the code. Type "exit" in the terminal to exit the code.')
#Name
Name = input("Please enter your name: ").strip()
#Score (0)
Score = 0
print(f"Ok, I will remember your name as {Name}.")
#Invalid inputs (0)
InvalidInputs = 0
#Test1
print("Test 1: Is this a valid Python command?")
print("if")
print("elif")
print("else")
print("A) Only if and elif are valid commands.")
print("B) Only if and else are valid commands.")
print("C) All are valid commands.")
print("D) None are valid commands.")
print("E) Only else` is a valid command.")
print("F) Only elif is a valid command.")
Answer1 = input("Please enter your answer (A/B/C/D/E/F): ").strip().upper()
if Answer1 == "C":
    print("Correct! All are valid commands.🎉")
    Score += 1
    print(f"+1 score was added, you now have a total score of {Score}")
    print(f"{Name}, quick note, if you look at the code, you will see that i use if, elif, and else in the code.")
elif Answer1 in ["A", "B", "D", "E", "F"]:
    print("❌Incorrect. The correct answer is C) All are valid commands.")
    print(f"Your total score remains {Score}")
else:
    print("Invalid input. Please enter A, B, C, D, E, or F.")
    InvalidInputs += 1
    print("+1 invalid input was added.")
    print(f"Invalid input count: {InvalidInputs}")
#Test2
print("Test 2: What is the output of the following code?")
print("x = 5")
print("y = 15")
print("z = x * y")
print("print(z)")
print("A) 75")
print("B) 20")
print("C) 10")
print("D) 5")
Answer2 = input("Please enter your answer (A/B/C/D): ").strip().upper()
if Answer2 == "A":
    print("😁 Correct! The output is 75.")
    print(f"{Name}, the reason why is that * = multiplication, so 5 * 15 = 75.")
    Score += 1
    print(f"+1 score was added, you now have a total score of {Score}")
elif Answer2 in ["B", "C", "D"]:
    print("🫥 Incorrect. The correct answer is A) 75.")
    print(f"{Name}, the reason why is that * = multiplication, so 5 * 15 = 75.")
    print(f"Your total score remains {Score}")
else:
    print("Invalid input. Please enter A, B, C, or D.")
    InvalidInputs += 1
    print("+1 invalid input was added.")
    print(f"Invalid input count: {InvalidInputs}")
#Test3
print("Test 3: What is the output of the following code?")
print('Coding Language = "Python"')
print('Coding Editor = "VS Code"')
print('Coding Lessons = "Coddy.tech"')
print('print(f"Hello I am learning {Coding Language} in {Coding Editor} thanks to {Coding Lessons}")')
print("A) A SyntaxError will occur.")
print("B) Hello I am learning Python in VS Code thanks to Coddy.tech.")
print("C) Hello I am learning {Coding Language} in {Coding Editor} thanks to {Coding Lessons}.")
print("D) Nothing")
Answer3 = input("Please enter your answer (A/B/C/D): ").strip().upper()
#We need this fsr
A = {}
if Answer3 == "B":
    print("💯% Correct! The output is Hello I am learning Python in VS Code thanks to Coddy.tech.")
    print(f"{Name}, the reason why is that f-strings allow you to embed expressions inside string literals, using curly braces {A}.")
    Score += 1
    print(f"+1 score was added, you now have a total score of {Score}")
elif Answer3 in ["A", "C", "D"]:
    print("😑 Incorrect. The correct answer is B) Hello I am learning Python in VS Code thanks to Coddy.tech.")
    print(f"{Name}, the reason why is that f-strings allow you to embed expressions inside string literals, using curly braces {A}.")
    print(f"Your total score remains {Score}")
else:
    print("Invalid input. Please enter A, B, C, or D.")
    InvalidInputs += 1
    print("+1 invalid input was added.")
    print(f"Invalid input count: {InvalidInputs}")
#Test4
print("Test 4: What is the execution of the following code?")
print("exit()")
print("(Or quit()")
print('A) A error, you need print("exit()") for it to show up in the terminal.')
print("B) The code will exit the program.")
print("C) The code will exit the program and print 'exit()' in the terminal.")
print("D) Nothing will happen.")
Answer4 = input("Please enter your answer (A/B/C/D): ").strip().upper()
if Answer4 == "B":
    print("☺️ Correct! The code will exit the program.")
    Score += 1
    print(f"+1 score was added, you now have a total score of {Score}")
elif Answer4 in ["A", "C", "D"]:
    print("🙅🏻 Incorrect. The correct answer is B) The code will exit the program.")
    print(f"Your total score remains {Score}")
else:
    print("Invalid input. Please enter A, B, C, or D.")
    InvalidInputs += 1
    print("+1 invalid input was added.")
    print(f"Invalid input count: {InvalidInputs}")
#Test5 
print("Test 5: What is the error in the following code?")
print("2ndAnswer = Hello, world!")
print('print(2ndAnswer)')
print("SyntaxError: *Hidden*")
print('A) There is no existing variable called "2ndAnswer".There is only a varible called "Name".')
print("B) There is no error!")
print("C) The variable name cannot start with a number.")
print("D) The variable cannot have a = sign in it.")
Answer5 = input("Please enter your answer (A/B/C/D): ").strip().upper()
if Answer5 == "C":
    print("🙂‍↔️ Correct! The variable name cannot start with a number.")
    Score += 1
    print(f"+1 score was added, you now have a total score of {Score}")
elif Answer5 in ["A", "B", "D"]:
    print("😓 Incorrect. The correct answer is C) The variable name cannot start with a number.")
    print(f"Your total score remains {Score}")
else:
    print("Invalid input. Please enter A, B, C, or D.")
    InvalidInputs += 1
    print("+1 invalid input was added.")
    print(f"Invalid input count: {InvalidInputs}")
#ShowScore
print(f"Your total score is {Score} out of 5.")
if Score == 5:
    print("👌🏻You got a perfect 100%!")
elif Score == 4:
    print("😎You got a 80%!")
elif Score == 3:
    print("🙂You got a 60%!")
elif Score == 2:
    print("😐You got a 40%!")
elif Score == 1:
    print("😕You got a 20%! But you tried!")
else:
    print("😓You got a 0%! But you tried!")
#ShowInvalidInputs
print(f"You had a total of {InvalidInputs} invalid inputs.")
