import os
import sys

# Append the tools directory to the Python path
TOOLS_DIR = os.path.join(os.path.dirname(__file__), 'src', 'tlops_tools', 'tools')
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

import Preprocess

if __name__ == '__main__':
    Preprocess.main()
