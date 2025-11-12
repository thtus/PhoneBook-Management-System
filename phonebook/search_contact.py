from typing import List
from .models import Contact

def search_by_name(store: List[Contact], q: str) -> List[Contact]:
    """Case-sensitive substring match by full_name."""
    return [c for c in store if q in c.full_name]
