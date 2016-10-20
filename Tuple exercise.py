textbooks = [("textbook ID", "Textbook Name", "Course", " # of Books", "Price per Book", "Publisher ID"),
             ("TEXT-0001", "Basic Anatomy and Physiology", "BIO-100", 400, 94.00, "PUB-1003"),
             ("TEXT-0002", "Chemistry for Biology Students", "BIO-101-102", 400, 105.30, "PUB-1002"),
             ("TEXT-0003", "Anatomy and Physiology", "BIO-141-142", 330, 159.75, "PUB-1003")]
publisher = [("Publisher ID", "Publisher Name", "Address", "City", "State", "Zip", "Phone Number"),
             ("PUB-1001", "Science Books Galore", "525 Allen St", "Trenton", "NJ", "08620", "609-555-2554"),
             ("PUB-1002", "Books for Chemestry Students Ltd", "142 N Spring St", "Los Angel", "CA", "90012", "213-555-8382"),
             ("PUB-1003", "Carliz Publishers Corp", "24 King Ave", "Columbus", "OH", "43201", "614-555-3322")]
t = 0
txt = []
while t < len(textbooks):
    txt.append(textbooks[t][1])
    txt.append(textbooks[t][1])
    t += 1
    print txt
txt = []

p = 0
pub = []
while p < len(publisher):
    pub.append(publisher[p][1])
    pub.append(publisher[p][6])
    p += 1
    print pub
pub = []
