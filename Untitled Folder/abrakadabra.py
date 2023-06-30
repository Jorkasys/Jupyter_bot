import csv

input_file = "fashion_products.csv"
data = []
f_names = None

# Reading data from csv file
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    f_names = reader.fieldnames
    for row in reader:
        data.append(row)


def safe_input(input_type, message):
    while True:  # Until the user enters a valid value
        value = input(message)
        if type(input_type) == int:
            if str(value).isdigit() is False:
                print('Unclassified input! Enter a number!')
            else:
                break
        if type(input_type) == str:
            if str(value).isalpha() is False:  # all my inputs don't require mixed format(dora111) so this works
                print('Unclassified input! Enter a words!')
            else:
                break
        if type(input_type) == float:
            try:
                value = float(value)
                break
            except Exception:
                print('Unclassified input! Enter a number!')
    return value


def writer_to_csv(ans, filename):  # the arguments are the rows that we need and the file name
    csv_file = filename
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=ans)  # working with rows
        writer.writeheader()
        writer.writerow(ans)


# Search for the best (price + rating) clothes of a certain category
def best_thing():
    gender = str(safe_input("str", "For whom we choose an outfit? (W or M)"))
    while gender not in 'MW':
        print('please write your answer in the correct format')
        gender = safe_input("str", "For whom we choose an outfit? (W or M)")
    if gender == "W":
        gender = "Women's Fashion"
    else:
        gender = "Men's Fashion"
    size = safe_input("str", "what should be the size?(S, M, L, XS, XL...): ")
    product_name = safe_input("str", "Please, enter the clothing category(Dress, Jeans, Shoes, T-shirt, Sweater...): ")
    min_cost = 9999 # to always go into 1 iteration
    max_mark = 0.1
    for row in data[0:]: # 0 element - title
        if (
                str(row['Category']) == gender and
                str(row['Size']) == size and
                str(row['Product Name']) == product_name and
                int(row['Price']) < min_cost and # the lower the cost, the better the item for the buyer
                round(float(row['Rating']), 5) > max_mark): # the higher the rating, the better the item for the buyer
            min_cost = int(row['Price'])
            max_mark = round(float(row['Rating']), 5)
            ans = row
    writer_to_csv(ans, 'best.csv') # I call the write function and pass a dictionary with the necessary data there
    return (ans)


# Поиск ботинок штанов и верхней одежды нужных цветов
def searching_set():
    gender = str(safe_input("str", "For whom we choose an outfit? (W or M)"))
    while gender not in 'MW':
        print('please write your answer in the correct format')
        gender = safe_input("str", "For whom we choose an outfit? (W or M)")
    if gender == "W":
        gender = "Women's Fashion"
    else:
        gender = "Men's Fashion"
    size = safe_input("str", "what should be the size?(S, M, L, XS, XL...): ")
    color_shoes = safe_input("str", "Please, enter the color of shoes(Black, Green, White, Blue): ")
    color_legs = safe_input("str", "Please, enter color of trousers(Black, Green, White, Blue): ")
    color_top = safe_input("str", "Please, enter the color of outerwear(Black, Green, White, Blue): ")
    clothes = {'shoes': [], 'legs': [], 'top': []} # in this dictionary items of clothing are sorted by
    # group which makes it easier to select
    for row in data[0:]:
        if (
                str(row['Category']) == gender and
                str(row['Size']) == size):
            if (str(row['Product Name']) == 'Shoes') and (str(row['Color']) == color_shoes):
                clothes['shoes'] += [row['Brand'], row['Price'], round(float(row['Rating']), 2)] # add the necessary
                # set items to dictionary rounding rating for user convenience
            elif (str(row['Product Name']) == 'Jeans') and (str(row['Color']) == color_legs):
                clothes['legs'] += [row['Brand'], row['Price'], round(float(row['Rating']), 2)]
            elif (str(row['Product Name']) in ['T-shirt', 'Sweater', 'Dress']) and (str(row['Color']) == color_top):
                clothes['top'] += [row['Brand'], row['Price'], round(float(row['Rating']), 2)]
    print(f"{clothes['shoes']}")
    print(clothes['legs'])
    print(clothes['top'])
    writer_to_csv(clothes, 'set.csv')


# Search for a specific thing by many parameters
def searching_clothes():
    product_name = safe_input("str", "Please, enter the clothing category(Dress, Jeans, Shoes, T-shirt, Sweater...): ")
    brand = safe_input("str", "Please, enter the brand(Zara, H&M, Adidas, Gucci...): ")
    gender = str(safe_input("str", "For whom we choose an outfit? (W or M)"))
    while gender not in 'MW':
        print('please write your answer in the correct format')
        gender = safe_input("str", "For whom we choose an outfit? (W or M)")
    if gender == "W":
        gender = "Women's Fashion"
    else:
        gender = "Men's Fashion"
    price = safe_input(1, "Please, enter the the largest amount (in $): ")
    rating = safe_input(1.3, "What should be the minimum rating?(from 1.0 up to 5.0): ")
    color = safe_input("str", "What should be the color?(Black, Green, White, Blue): ")
    size = safe_input("str", "what should be the size?(S, M, L, XS, XL...): ")
    needed_clothes = {}
    for row in data[0:]:
        if (
                str(row['Product Name']) == product_name and
                str(row['Brand']) == brand and
                str(row['Category']) == gender and
                int(row['Price']) <= int(price) and
                float(row['Rating']) >= float(rating) and
                str(row['Color']) == color and
                str(row['Size']) == size
        ):
            needed_clothes.update(row) # "add" dictionaries to pass it later to the write function in csv
    writer_to_csv(needed_clothes, 'a.csv')
    print(needed_clothes)


searching_clothes()
