# აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:
# Person:
# name
# deposit (default value = 1000, მიუთითებს ამჟამად რამდენი 
# აქვს დეპოზიტზე)
# loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს 
# ესხი აღებული)
# House:
# ID – ბინის საკატასტრო კოდი
# price – ბინის ფასი

# owner – სახლის მეპატრონე (Person ტიპის ობიექტი)

# status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის 
# “გასაყიდი”

# გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის 
# ობიექტი

# Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს 
# პიროვნების სრულ ინფორმაციას

# შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი 
# მეპატრონე, მეორე მყიდველი). ასევე შექმენით House კლასის 
# ობიექტი რომლის owner იქნება ერთ-ერთი Person ობიექტი

# House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის 
# დროსაც პარამეტრებად გადაეცემა მყიდველი, თუ მეტი 
# პარამეტრი არ გადაეცემა, ამ დროს უნდა შესრულდეს ბინის 
# გაყიდვის ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს 
# ბინის ღირებულებით, უნდა შეიცვალოს owner და status უნდა
#  გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი). თუ ამ
#  მეთოდის გამოძახების დროს მყიდველის გარდა პარამეტრად
#  გადაეცა კიდევ ერთი რიცხვი, მაშინ შესრულდეს ბინის სესხით
#  გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი 
# მიუთითებს მყიდველის მიერ აღებული სესხის რაოდენობას,
#  მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: 
# გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით,
# owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”, 
# მყიდველის სესხი (loan) უნდა გაიზარდოს შესაბამისი 
# რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.

# კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახებ

class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit},
        Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"
    def sell(self, buyer, loan_amount=0):
        self.owner.deposit += self.price
        self.owner = buyer
        if loan_amount > 0:
            self.status = "sold on loan"
            buyer.loan += loan_amount
        else:
            self.status = "sold"
        print(f"House {self.ID} sold to {buyer.name}. New deposit:
        {buyer.deposit}, New status: {self.status}")
    
    def __str__(self):
        return f"ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name},
        Status: {self.status}"


owner = Person(name = "John Doe", deposit=5000)
buyer = Person(name = "Jane Smith", deposit=3000)


house = House(ID = 123, price = 100000, owner = owner)
house.sell(buyer)
house.sell(buyer, loan_amount=5000)

print(owner)
print(buyer)
print(house)