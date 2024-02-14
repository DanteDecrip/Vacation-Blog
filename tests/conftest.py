import sys
import pathlib

import pytest

# Unfortunately, this needs to happen first.
test_dir = pathlib.Path(__file__).parent

sys.path.append(str(test_dir.parent.absolute()))
print(sys.path)
