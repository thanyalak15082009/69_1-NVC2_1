def Products(name, price):
    # คำนวณ เหนือ
    vat = price * 0.07
    # นันท์นภัส
    total_price= price + vat
    
    print(f"ชื่อสินค้า: {name}")
    print(f"ราคาสินค้า: {price:.2f} บาท")
    print(f"ภาษี VAT 7%: {vat:.2f} บาท")
    print(f"ราคารวมภาษี (สุทธิ): {total_price:.2f} บาท\n")
# รับข้อมูล เหนือ    
for i in range(1, 6):
    print(f"กรุณากรอกข้อมูลสินค้าชิ้นที่ {i}")
    product_name = input("ชื่อสินค้า: ")
    product_price = float(input("ราคาสินค้า: "))
    
    # เรียกใช้ เหนือ
    Products(product_name, product_price)