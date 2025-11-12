# test_phonebook.py  (chỉ để thử, không phải main của dự án)
from phonebook.models import Contact
from phonebook.add_contact import add_contact
from phonebook.edit_contact import edit_contact
from phonebook.delete_contact import remove_contact
from phonebook.search_contact import search_by_name
from phonebook.data_manager import save_contacts_json, load_contacts_json

store = []

# 1) Thêm liên hệ
ok, reason = add_contact(store, Contact(id="1", full_name="Nguyen Van A",
                                        phones=["+84 912345678"], email="a@gmail.com"))
print("Add #1:", ok, reason)

# 2) Thêm trùng id (để thấy báo lỗi)
ok, reason = add_contact(store, Contact(id="1", full_name="Duplicate"))
print("Add duplicate:", ok, reason)

# 3) Tìm kiếm theo tên
results = search_by_name(store, "Nguyen")
print("Search 'Nguyen':", [c.full_name for c in results])

# 4) Sửa thông tin
ok, reason = edit_contact(store, "1", Contact(id="1", full_name="Nguyen Van A (Updated)"))
print("Edit #1:", ok, reason)

# 5) Lưu ra JSON
save_contacts_json(store, "contacts.json")
print("Saved -> contacts.json")

# 6) Load lại từ JSON để chắc
loaded = load_contacts_json("contacts.json")
print("Loaded:", [c.full_name for c in loaded])

# 7) Xóa
removed = remove_contact(store, "1")
print("Remove #1:", removed)
