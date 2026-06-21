def add_product(products):
    product_id = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    try:
        price = float(input("Nhập giá sản phẩm: "))
        if price < 0:
            raise ValueError("Giá âm")
        stock = int(input("Nhập số lượng tồn kho ban đầu: "))
        if stock < 0:
            raise ValueError("Số lượng tồn kho không được âm")
    except ValueError as e:
        print(f"Lỗi nhập dữ liệu: {e}")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    products.append(product)
    print("Thêm sản phẩm mới vào kho thành công!")

def find_product(products, product_id):
    for p in products:
        if p['id'] == product_id:
            return p
    return None

def import_stock(products):
    product_id = input("Nhập mã sản phẩm nhập hàng: ")
    p = find_product(products, product_id)
    if not p:
        print("Sản phẩm không tồn tại trong kho.")
        return
    try:
        quantity = int(input("Nhập số lượng muốn nhập thêm: "))
        if quantity <= 0:
            raise ValueError("Số lượng nhập phải lớn hơn 0")
        p['stock'] += quantity
        print("Nhập hàng thành công!")
    except ValueError as e:
        print(f"Lỗi nhập hàng: {e}")

def export_stock(products):
    product_id = input("Nhập mã sản phẩm xuất hàng: ")
    p = find_product(products, product_id)
    if not p:
        print("Sản phẩm không tồn tại trong kho.")
        return
    try:
        quantity = int(input("Nhập số lượng muốn xuất: "))
        if quantity <= 0:
            raise ValueError("Số lượng xuất phải lớn hơn 0")
        if quantity > p['stock']:
            raise ValueError("Xuất quá số lượng tồn kho")
        p['stock'] -= quantity
        print("Xuất hàng thành công!")
    except ValueError as e:
        print(f"Lỗi xuất hàng: {e}")

def display_products(products):
    if not products:
        print("Kho hàng trống.")
        return
    for p in products:
        print(f"{p['id']} - {p['name']} - Giá: {p['price']:,}đ - Tồn kho: {p['stock']}")

def calculate_inventory_value(products):
    return sum(p['price'] * p['stock'] for p in products)

def sort_products(products):
    products.sort(key=lambda p: p['price'])
    print("Đã sắp xếp sản phẩm theo giá tăng dần.")
    display_products(products)

def main_bai3():
    products = []
    while True:
        print("\n===== WAREHOUSE MANAGEMENT =====")
        print("1. Nhập hàng (Thêm số lượng vào sản phẩm có sẵn hoặc tạo mới tùy chọn số 1 ngoài menu chính)")
        print("2. Xuất hàng")
        print("3. Tìm sản phẩm")
        print("4. Xem tồn kho")
        print("5. Tính tổng giá trị kho")
        print("6. Sắp xếp theo giá")
        print("0. Thoát")
        
        choice = input("Chọn chức năng: ")
        match choice:
            case "1":
                print("1a. Tạo mới sản phẩm hoàn toàn")
                print("1b. Nhập thêm số lượng cho sản phẩm hiện có")
                sub_choice = input("Chọn (a/b): ")
                if sub_choice.lower() == 'a':
                    add_product(products)
                elif sub_choice.lower() == 'b':
                    import_stock(products)
                else:
                    print("Lựa chọn sai.")
            case "2":
                export_stock(products)
            case "3":
                product_id = input("Nhập mã sản phẩm cần tìm: ")
                p = find_product(products, product_id)
                if p:
                    print(f"Tìm thấy: {p['id']} - {p['name']} - Giá: {p['price']:,}đ - Tồn kho: {p['stock']}")
                else:
                    print("Không tìm thấy sản phẩm.")
            case "4":
                display_products(products)
            case "5":
                total_value = calculate_inventory_value(products)
                print(f"Tổng giá trị kho hàng: {total_value:,} đ")
            case "6":
                sort_products(products)
            case "0":
                print("Thoát chương trình quản lý kho.")
                break
            case _:
                print("Lựa chọn không hợp lệ.")