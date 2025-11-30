"""
SEVE Framework Compatibility Layer
Redirects imports from 'seve' to 'seve_framework' for backward compatibility.
"""

import sys
import logging

# Configurar logger
logger = logging.getLogger(__name__)
logger.warning("Importing from 'seve' is deprecated. Please use 'seve_framework' instead.")

# Importar componentes principais do novo framework
try:
    from seve_framework.core import SEVECoreV3 as SEVECore
    from seve_framework.config import SEVEConfig
    from seve_framework.ethics import SEVEEthicsModule as SEVEEthics
    from seve_framework.ethics import SEVEEthicsModule as EthicsEngine # Alias legado
    from seve_framework.universal.empathy import UniversalEmpathyEngine as EmpathyModule
except ImportError as e:
    logger.error(f"Failed to import seve_framework components: {e}")
    # Fallback vazio para não quebrar instalação se dependências faltarem
    class SEVECore: pass
    class SEVEConfig: pass
    class SEVEEthics: pass
    class EthicsEngine: pass
    class EmpathyModule: pass

# Expor versão
__version__ = "1.0.0-beta"
