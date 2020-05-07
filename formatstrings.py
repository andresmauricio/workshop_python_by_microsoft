first_name = 'Andres'
last_name = 'Acelas'

output_bad = print('Hello' + ' ' + first_name + ' ' + last_name)
output_format = print('Hello {} {}'.format(first_name, last_name))
output_format_specific = print('Hello {0} {1}'.format(first_name, last_name))

#Version >= 3
output_format_good = print(f'Hello {first_name} {last_name}')