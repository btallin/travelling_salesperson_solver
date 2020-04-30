from travelling_salesperson.solver import solve

best_path = solve(
    addresses=(
        "The White House, Washington, DC",
        "30 Rockefeller Plaza, New York City, New York",
        "Las Vegas Boulevard, Las Vegas, NV",
        "1600 Amphitheatre Pkwy, Mountain View, CA",
    ),
    start_anywhere=False,
    end_anywhere=False
)
print(best_path)
