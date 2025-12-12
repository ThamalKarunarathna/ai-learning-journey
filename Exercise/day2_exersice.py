
#exercise A
movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]

print("Movie List:")
for movie in movies:
    print("-", movie)

movies.append("Fight Club")
print("\nUpdated Movie List:")
for movie in movies:
    print("-", movie)

movies.remove("Pulp Fiction")
print("\nAfter Removal Movie List:")
for movie in movies:
    print("-", movie)


#exercise B

my_profile = {
    "name" : "John Doe",
    "age" : 28,   
    "occupation" : "Software Developer",
    "country" : "USA"
}

print("\nMy Profile:")
for key, value in my_profile.items():
    print(key, ":", value)


#exercise C

for i in range(0, 20):
    if i % 2 == 0:
        print("Number:", i)

