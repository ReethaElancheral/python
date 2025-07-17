import sys, os
import pprint

pprint.pprint(sys.path)
sys.path.append(os.path.join(os.getcwd(), "extra"))
pprint.pprint(sys.path)
