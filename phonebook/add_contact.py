from typing import List, Tuple
from .models import Contact
from .validator import is_contact_basic_ok

def add_contact(store: List[Contact], c: Contact) -> Tuple[bool, str]:
    """Append new contact if valid and id unique."""
    ok, reason = is_contact_basic_ok(c)
    if not ok:
        return False, reason
    if any(x.id == c.id for x in store):
        return False, "id duplicated"
    store.append(c)
    return True, ""
