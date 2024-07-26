from pathlib import Path
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR,'Media/')
print(MEDIA_ROOT)