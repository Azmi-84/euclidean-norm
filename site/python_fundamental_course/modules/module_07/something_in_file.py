def greeting(name):
	print(f'Hello {name}')

name = ['abcd', 'abcd', 'abcd', 'abcd', 'abcd']
person = {key: name for key, name in zip(range(len(name)), name)}
print(person)