def unlimited_functions(*args, **keyword_args):
    print(keyword_args)
    for k, arguments in keyword_args.items():
        print(k, arguments)

unlimited_functions(1,2,3,4, name = 'jackson', age = 37)