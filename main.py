from datetime import datetime

def param_decor(log_file_path):
	def decor(foo):
		def new_foo(*args, **kwargs):
			f = open(log_file_path, 'a')
			time_stamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
			result = foo(*args, **kwargs)
			log_entry = f'DATE/TIME: {time_stamp}\tFUNCTION NAME: {foo.__name__}\tARGS: {args}\tRESULT: {result}'
			f.write(log_entry + '\n')
			f.close()
			return result
		return new_foo
	return decor

@param_decor('log.txt')
def add(a, b):
	return a + b

print(add(4, 4))

@param_decor('log.txt')
def flatten(list):
	for el1 in list:
		for el2 in el1:
			yield el2

nested_list = [['a', 'b', 'c'],['d', 'e', False],[1, None]]
print(list(flatten(nested_list)))