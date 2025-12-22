#KBC Programm
#This is a basic KBC like programm
def user_answers(scan):
    while True:
        entered_option= input("enter the option").upper()
        if entered_option == scan["ans"]:
            total_winnings = scan["prize"]
            print("Congratulation This is Correct Answer\nYou Have Won RS.",total_winnings)
            break


        elif entered_option not in ("A","B","C","D"):
            print("Wrong Command")
            print("Please Try Again")
            continue

        else:
            print("This is incorrect\nSorry but your journey ends here")
            exit()
def ask_questions(scan):
    print(scan["q"])
    print("Here are the options : ")
    for opt in scan["option"]:
        print(opt)
def user_input():
    while True:
        if (index1 == last):
            break
        given_input = input("Do you wish to continue(y/n)").upper()
        if (given_input == "Y"):
                print("lets go")
                break

        elif (given_input == "N"):
            print("OK We Understand It Was Fun To Play With You")
            print(f"Your Winnings are : {Current_winnings}")
            exit()

        if given_input not in ("Y","N"):
            print("Wrong Command\nTry Again")
            continue



print("Welcome To The Kon Banega CrorePati\nLets Start The Game")
def start():
    while True:
        a = input("shall we start (y/n)").upper()
        if(a == "Y"):
            print("lets start")
            break
        elif(a == "N"):
            print("OK We Can Play Later")
            return False
            break
        else:
            print("Wrong Command\nTry Again")
            continue
input1 = start()
if (input1 == False):
    exit()

print("just enter the option")
question = [    {"q" : "Q1.) For the First Question\nWho is known as the Father of the Indian Constitution?",
    "option" :
    [ "A) Mahatma Gandhi\n",
      "B) Jawaharlal Nehru\n",
      "C) B. R. Ambedkar\n",
      "D) Rajendra Prasad\n"],
    "ans" : "C",
    "prize" : 5000
    },
    {
     "q" : "Q2.)Which planet is called the Red Planet?",
    "option" :  [
      "A) Venus\n",
      "B) Mars\n",
      "C) Jupiter\n",
      "D) Saturn\n"],
    "ans" : "B",
    "prize" : 10000
    },
    {
    "q" : "Q3.)The national animal of India is : ",
    "option" :  [
      "A) Lion\n",
      "B) Elephant\n",
      "C) Tiger\n",
      "D) Leopard\n"],
    "ans" : "C",
    "prize" : 20000
    },
    {
    "q" : "Q4.) Which Indian state has the longest coastline? ",
    "option" :  [
      "A) Tamil Nadu\n",
      "B) Andhra Pradesh\n",
      "C) Gujarat\n",
      "D) Maharashtra\n"],
    "ans" : "C",
    "prize" : 40000
    },
    {
    "q" : "Q5.)How many players are there in a cricket team (on field)? ",
    "option" :  [
      "A) 8\n",
      "B) 10\n",
      "C) 11\n",
      "D) 15\n"],
    "ans" : "C",
    "prize" : 80000
    },
    {
    "q" : "Q6.)The currency of Japan is:",
    "option" :  [
      "A) Won\n",
      "B) Yen\n",
      "C) Yuan\n",
      "D) Ringgit\n"],
    "ans" : "B",
    "prize" : 120000
    },
    {
    "q" : "Q7.)Who was the first woman Prime Minister of India?",
    "option" :  [
      "A) Pratibha Patil\n",
      "B) Sarojini Naidu\n",
      "C) Indira Gandhi\n",
      "D) Sucheta Kriplani\n"],
    "ans" : "C",
    "prize" : 200000
    },
    {
    "q" : "Q8.) Which gas is most abundant in Earth’s atmosphere?",
    "option" :  [
      "A) Oxygen\n",
      "B) Nitrogen\n",
      "C) Carbon dioxide\n",
      "D) Hydrogen\n"],
    "ans" : "B",
    "prize" : 240000
    },
    {
    "q" : "Q9.)Which Fundamental Right is abolished during a National Emergency?",
    "option" :  [
      "A) Right to Equality\n",
      "B) Right to Freedom\n",
      "C) Right against Exploitation\n",
      "D) Right to Constitutional Remedies\n"],
    "ans" : "D",
    "prize" : 480000
    },
    {
    "q" : "Q10.) Who wrote the book “Discovery of India”?",
    "option" :  [
      "A) Jawaharlal Nehru\n",
      "B) Sardar Patel\n",
      "C) Rabindranath Tagore\n",
      "D) Mahatma Gandhi\n"],
    "ans" : "A",
    "prize" : 1000000
    },
    {
    "q" : "Q11.) The unit of electrical resistance is:",
    "option" :  [
      "A) Volt\n",
      "B) Ampere\n",
      "C) Ohm\n",
      "D) Watt\n"],
    "ans" : "C",
    "prize" : 2500000
    },
    {
    "q" : "Q12.) Which Indian mission successfully reached Mars in its first attempt?",
    "option" :  [
      "A) Gaganyaan\n",
      "B) Mangalyaan\n",
      "C) Aditya-L1\n",
      "D) Chandrayaan-1\n"],
    "ans" : "B",
    "prize" : 5000000
    },
    {
    "q" : "Q13.) Who is known as the Missile Man of India?",
    "option" :  [
      "A) A. P. J. Abdul Kalam\n",
      "B) Homi Bhabha\n",
      "C) Satish Dhawan\n",
      "D) Vikram Sarabhai\n"],
    "ans" : "A",
    "prize" : 10000000
    },
    {
    "q" : "Q14.) The term “Blue Economy” is related to: ",
    "option" :  [
      "A) Renewable energy\n",
      "B) Marine resources & oceans\n",
      "C) Banking reforms\n",
      "D) Space technology\n"],
    "ans" : "B",
    "prize" : 70000000
    }
 ]
Current_winnings = 0
last = len(question) - 1
for index1, length1 in enumerate(question):
    ask_questions(length1)
    user_answers(length1)
    Current_winnings = length1["prize"]
    user_input()
    if(index1 == last):
        print("you have won the game\nYou Are Now Crore Pati")






