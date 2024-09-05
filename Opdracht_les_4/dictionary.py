movies_and_numbers = {
    "The Simpsons": "636-555-3226",
    "Vegas Vacation": "555-0100",
    "Ghostbusters": "555-23678",
    "Billy Madison": "555-0840",
    "Swingers": "213-555-4679",
    "Bruce Almighty": "555-0123",
    "Seinfeld": "555-FILK",
    "Arrested Development": "555-0113",
    "Die Hard With a Vengeance": "555-0001",
    "The A-Team": "555-6162"
}
print(movies_and_numbers)

print(f"Het telefoonnummer van Bruce Almighty is {movies_and_numbers["Bruce Almighty"]}.")
movies_and_numbers["Harry Potter"] = "605-475-6961"
print(movies_and_numbers["Harry Potter"])

old_number = movies_and_numbers["Ghostbusters"]
movies_and_numbers["Ghostbusters"] = "555-2368"
print(f"Het telefoonnummer {old_number} van de Ghostbusters is gewijzigd naar {movies_and_numbers["Ghostbusters"]}.")

deleted_number = movies_and_numbers["Seinfeld"]
movies_and_numbers.pop("Seinfeld")
print(f"Telefoonnummer {deleted_number} van Seinfeld is verwijderd.")
print(movies_and_numbers)

print(f"In de dictionary zitten {len(movies_and_numbers)} telefoonnummers.")
print(movies_and_numbers)