# String methods("")
question = "Would you please help me?"

#upper
print(question.upper())

#lower
print(question.lower())

#endswith
print(question.endswith("?"))

#startswith
print(question.startswith("Would"))

#replace
print(question.replace("me",""))

#index
print(question.index("please"))
print(question.index("p"))

#find
print(question.find("you"))
print(question.find("joy"))

#remove prefix
print(question.removeprefix("Would you"))

#remove suffix
print(question.removesuffix("help me?"))


#split
print(question.split())

idea = "   it is my idea   "

#strip
print(idea.strip())

#left strip
print(idea.lstrip())

#right strip
print(idea.rstrip())

#count
print(idea.count())