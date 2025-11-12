import json
from typing import List
from .models import Contact

def save_contacts_json(contacts: List[Contact], filepath: str) -> None:
    """Write contacts to a JSON file (.json)."""
    payload = {
        "contacts": [c.to_dict() if isinstance(c, Contact) else Contact.from_dict(c).to_dict() for c in contacts]
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def load_contacts_json(filepath: str) -> List[Contact]:
    """Read contacts from JSON file and return list[Contact]."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = json.load(f)
    out: List[Contact] = []
    for j in raw.get("contacts", []):
        out.append(Contact.from_dict(j))
    return out
