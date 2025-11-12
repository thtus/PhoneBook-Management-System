from typing import List, Tuple
from .models import Contact
from .validator import is_contact_basic_ok

def edit_contact(store: List[Contact], id: str, patch: Contact) -> Tuple[bool, str]:
    """Patch contact by id with non-empty fields from `patch`."""
    for i, x in enumerate(store):
        if x.id == id:
            tmp = Contact(
                id=x.id,
                full_name=patch.full_name or x.full_name,
                phones=patch.phones or x.phones,
                email=patch.email or x.email,
                address=patch.address or x.address,
                relationship=patch.relationship or x.relationship,
                notes=patch.notes or x.notes,
            )
            ok, reason = is_contact_basic_ok(tmp)
            if not ok:
                return False, reason
            store[i] = tmp
            return True, ""
    return False, "not found"
