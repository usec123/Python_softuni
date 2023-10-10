def concatenate(*args, **kwargs):
    concatenated_args = ''.join(args)
    
    for key,value in kwargs.items():
        if key in concatenated_args:
            concatenated_args = concatenated_args.replace(key,value)
    return concatenated_args

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))