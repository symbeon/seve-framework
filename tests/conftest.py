"""Pytest configuration and fixtures."""

import sys
from pathlib import Path
from unittest.mock import MagicMock, Mock

# Mock missing dependencies BEFORE any imports
# This prevents ImportError when seve_framework modules try to import these

_mock_cv2 = MagicMock()
_mock_cv2.VideoCapture = Mock()
_mock_cv2.imread = Mock()
_mock_cv2.imwrite = Mock()
sys.modules['cv2'] = _mock_cv2

_mock_torch = MagicMock()
_mock_torch.Tensor = Mock
sys.modules['torch'] = _mock_torch
sys.modules['torch.nn'] = MagicMock()
sys.modules['torch.optim'] = MagicMock()

_mock_numpy = MagicMock()
sys.modules['numpy'] = _mock_numpy
sys.modules['numpy.ndarray'] = Mock

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Pytest markers
import pytest

pytest_plugins = []

