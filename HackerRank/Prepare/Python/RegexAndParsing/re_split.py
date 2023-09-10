# %% Itertools solution
regex_pattern = r"\W"	# Do not delete 'r'.

import re
input_str = '100,000,000.000'
print("\n".join(re.split(regex_pattern, input_str)))