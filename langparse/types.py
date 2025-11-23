from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class Chunk:
    """
    Represents a chunk of text derived from a document.
    """
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Document:
    """
    Represents a parsed document.
    """
    content: str  # The full text content (usually Markdown)
    metadata: Dict[str, Any] = field(default_factory=dict)
    chunks: List[Chunk] = field(default_factory=list)
