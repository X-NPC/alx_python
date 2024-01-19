# All of it is copy-pasted from my friend's code so it atleast 
# needs to be studied and revised 

def best_score(a_dictionary):
 if not a_dictionary:
  return None
 max_key = None
 max_value = float('-inf')
 for key, value in a_dictionary.items():
  if value > max_value:
   max_key = key
   max_value = value
 return max_key
