# -*- coding: UTF-8 -*-

# response_body = [
#     '%s: %s' % (key, value) for key, value in sorted(environ.items())
# ]
# response_body = '\n'.join(response_body)

# response_body = [
#     'The Beggining\n',
#     '*' * 30 + '\n',
#     "hello world\n",
#     '\n' + '*' * 30,
#     '\nThe End'
# ]

response_body = [
    '1',
    '2'
]

# 求Content-Length
content_length = sum([len(s) for s in response_body])

print content_length