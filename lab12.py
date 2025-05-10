# Дані товарів
products = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 25000, "категорія": "електроніка"},
    {"назва": "Миша", "кількість": 50, "ціна": 400, "категорія": "електроніка"},
    {"назва": "Футболка", "кількість": 20, "ціна": 300, "категорія": "одяг"},
    {"назва": "Хліб", "кількість": 30, "ціна": 25, "категорія": "продукти"},
    {"назва": "Молоко", "кількість": 5, "ціна": 35, "категорія": "продукти"},
    {"назва": "Кросівки", "кількість": 8, "ціна": 1500, "категорія": "одяг"},
    {"назва": "Монітор", "кількість": 4, "ціна": 6000, "категорія": "електроніка"},
]

# Функція для виводу таблиці
def print_table(data):
    print(f"{'Назва':<15} {'Кількість':<10} {'Ціна':<10} {'Категорія':<15}")
    print("-" * 50)
    for item in data:
        print(f"{item['назва']:<15} {item['кількість']:<10} {item['ціна']:<10} {item['категорія']:<15}")

# Виведення структури
print("Список товарів:")
print_table(products)

# --- Завдання 2: Пошук та редагування ---
def find_product_by_name(name):
    for product in products:
        if product["назва"].lower() == name.lower():
            return product
    return None

def find_products_by_category(category):
    return [p for p in products if p["категорія"].lower() == category.lower()]

def update_product(product):
    print("Знайдено товар:")
    print_table([product])
    field = input("Що бажаєте оновити? (кількість/ціна): ").strip().lower()
    if field in ["кількість", "ціна"]:
        try:
            new_value = float(input(f"Нове значення для {field}: "))
            if new_value < 0:
                print("Помилка: значення не може бути від’ємним.")
                return
            product[field] = int(new_value) if field == "кількість" else new_value
            print("Товар оновлено:")
            print_table([product])
        except ValueError:
            print("Помилка: введено некоректне число.")
    else:
        print("Помилка: невідоме поле.")

# Демонстрація пошуку
choice = input("\nШукати товар за (назвою/категорією): ").strip().lower()
if choice == "назвою":
    name = input("Введіть назву товару: ")
    product = find_product_by_name(name)
    if product:
        update_product(product)
    else:
        print("Товар не знайдено.")
elif choice == "категорією":
    cat = input("Введіть назву категорії: ")
    found = find_products_by_category(cat)
    if found:
        print("Знайдені товари:")
        print_table(found)
    else:
        print("У цій категорії товарів не знайдено.")
else:
    print("Помилка: неправильний вибір.")

# --- Завдання 3: Аналітика ---
def inventory_analysis(products):
    category_totals = {}
    low_stock = []

    for product in products:
        total = product["кількість"] * product["ціна"]
        category = product["категорія"]
        category_totals[category] = category_totals.get(category, 0) + total

        if product["кількість"] < 5:
            low_stock.append(product)

    max_category = max(category_totals.items(), key=lambda x: x[1])

    print("\nЗагальна вартість по категоріях:")
    for category, total in category_totals.items():
        print(f"- {category}: {total:.2f} грн")

    print(f"\nКатегорія з найбільшою сумарною вартістю: {max_category[0]} ({max_category[1]:.2f} грн)")

    print("\nТовари, які потребують замовлення (менше 5 шт.):")
    if low_stock:
        print_table(low_stock)
    else:
        print("Усі товари в достатній кількості.")

# Виклик аналітики
inventory_analysis(products)
