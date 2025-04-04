# user_profile.py
# 🧑‍💻 Project: User Profile Manager (Tổng hợp tuần 1)

# Bước 1: Nhập thông tin người dùng
user_name = input("Hãy nhập tên của bạn: ")
user_birth = int(input("Hãy nhập năm sinh của bạn: "))
user_year = int(input("Nhập năm hiện tại: "))
user_py = input("Bạn có thích học Python không? Nhập Y là Có, N là Không: ")

# Bước 2: Tính tuổi và phân loại
user_age = user_year - user_birth
print("\n----------------------------")
print(f"📄 Bạn {user_name}, năm nay {user_age} tuổi.")

if user_age >= 60:
    print(f"{user_name} đã già 👵🧓")
elif 41 <= user_age <= 59:
    print(f"{user_name} gần về hưu và là bậc tiền bối trong xã hội")
elif 31 <= user_age <= 40:
    print(f"{user_name} đang tuổi trưởng thành 💼")
elif 19 <= user_age <= 30:
    print(f"{user_name} đang là tuổi thanh xuân rực rỡ ✨")
elif 12 <= user_age <= 18:
    print(f"{user_name} đang là tuổi teen 🧑‍🎓")
else:
    print(f"{user_name} đang là trẻ em 👶")

# Bước 3: Kiểm tra sở thích học Python
if user_py.lower() == "y":
    print(f"{user_name} ✅ Có thích học Python")
else:
    print(f"{user_name} ❌ Không thích học Python")
