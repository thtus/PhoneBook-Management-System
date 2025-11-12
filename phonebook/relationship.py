from typing import List, Tuple
from .models import Contact

def update_relationship(store: List[Contact], id: str, new_relation: str) -> Tuple[bool, str]:
    """Update a contact's relationship field."""
    for c in store:
        if c.id == id:
            c.relationship = new_relation or "Unknown"
            return True, ""
    return False, "contact not found"
