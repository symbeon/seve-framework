"""
SEVE Framework - Symbeon Ethical Vision Engine

Framework de IA ética para checkout inteligente, combinando:
- Detecção precisa de produtos (SEVE-Vision)
- Compliance ESG automático (SEVE-Ethics)
- Análise emocional (SEVE-Empathy)
- Personalização adaptativa (SEVE-Personality)
- Integração ERP (SEVE-Link)
- Sensores IoT (SEVE-Sense)
"""

from .core import SEVECore, SEVEContext
from .vision import SEVEVision
from .ethics import SEVEEthics
from .empathy import SEVEEmpathy
from .sense import SEVESense
from .link import SEVELink
from .personality import SEVEPersonality

__version__ = "1.0.0"
__author__ = "Symbeon Tech & GuardFlow Team"
__email__ = "research@symbeon.ai"

__all__ = [
    "SEVECore",
    "SEVEContext", 
    "SEVEVision",
    "SEVEEthics",
    "SEVEEmpathy",
    "SEVESense",
    "SEVELink",
    "SEVEPersonality",
]
