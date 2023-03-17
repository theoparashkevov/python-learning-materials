class CustomSet(set):
    def __new__(cls, *args, **kwargs):
        # Create a new set instance with the items sorted
        sorted_args = sorted(args[0]) if args else []
        return super().__new__(cls, sorted_args)

s = CustomSet([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(s)  # Outputs: {1, 2, 3, 4, 5, 6, 9}
