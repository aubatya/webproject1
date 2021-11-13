import string
import random
lu = []
lp = []
lo = []
alp = list(string.ascii_lowercase)
for k in range(1000):
        quantity_in_stock = random.randint(1, 1000000)
        pname = ""
        uname = ""
        surname = ""
        email = ""
        telephone = "+7"
        for i in range(random.randint(1, 9)):
            pname+=random.choice(alp)
        for i in range(random.randint(1, 9)):
            uname+=random.choice(alp)
        for i in range(random.randint(1, 9)):
            surname+=random.choice(alp)
        for i in range(random.randint(1, 9)):
            email+=random.choice(alp)
        for i in range(10):
            telephone+=str(random.randint(0, 9))
        description = ""
        for j in range(150):
            description+=random.choice(alp)
        address = ""
        for i in range(4):
            for j in range(random.randint(3, 7)):
                address+=random.choice(alp)
            address+=" "
        image = bin(random.randint(1, 100000000))
        price = random.uniform(1, 1000000)
        uname = uname.capitalize()
        surname = surname.capitalize()
        description = description.capitalize()
        pname = pname.capitalize()
        email+="@gmail.com"
        quantity = random.randint(1, 100000)
        product_id = random.randint(1, k+1)
        user_id = random.randint(1, k+1)
        odate = f"{str(random.randint(1, 28)).zfill(2)}.{str(random.randint(1, 12)).zfill(2)}.2021"
        ubdate = f"{str(random.randint(1, 28)).zfill(2)}.{str(random.randint(1, 12)).zfill(2)}.{random.randint(1900, 2020)}"
        usdate = f"{str(random.randint(1, 28)).zfill(2)}.{str(random.randint(1, 12)).zfill(2)}.2020"
        pdate = f"{str(random.randint(1, 28)).zfill(2)}.{str(random.randint(1, 12)).zfill(2)}.2019"
        lp.append((quantity_in_stock, pname, description, image, price, pdate))
        lu.append((uname, surname, email, telephone, ubdate, usdate))
        lo.append((address, quantity, product_id, user_id, odate))
with open("product.txt", "w") as f:
    print(f"INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES", file=f)
    for i in lp:
        print(f"{i},", file=f)
with open("user.txt", "w") as f:
    print(f"INSERT INTO user (name, surname, email, telephone, birth_date, start_date) VALUES", file=f)
    for i in lu:
        print(f"{i},", file=f)
with open("ordeer.txt", "w") as f:
    print(f"INSERT INTO ordeer (address, quantity, product_id, user_id, date) VALUES", file=f)
    for i in lo:
        print(f"{i},", file=f)