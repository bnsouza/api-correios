"""
Pydantic Schema - Todos os schemas que serão usados na API
"""

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field, constr

# Enums --------------------------------------------------------------------------------------------


class Ambiente(str, Enum):
    producao = "producao"
    homologacao = "homologacao"
