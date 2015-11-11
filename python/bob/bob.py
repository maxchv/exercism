#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    question = what.strip()
    if question.isupper():
      return "Whoa, chill out!"
    elif question.endswith('?'):
      return "Sure."
    elif len(question) == 0:
      return "Fine. Be that way!"
    else:
      return "Whatever."
