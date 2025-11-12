from typing import List
from .models import Contact

def remove_contact(store: List[Contact], id: str) -> bool:
    """Remove contact by id. Returns True if something removed."""
    old = len(store)
    store[:] = [c for c in store if c.id != id]
    return len(store) != old
