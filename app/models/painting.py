from pprint import pprint
from app.db import BaseModel

class Painting(BaseModel):

    SHEET_NAME = "painting"

    COLUMNS = ["title", "artist", "year","price","description","url"]

    SEEDS = [
        {
        "title": "Road with Cypress and Star", 
        "artist": "Dids", 
        "year": 2020,
        "price":1000,
        "description":"Modern Art", 
        "url":"static/images/image6.jpg"
        },
        {
            "title": "Les Grandes Baigneuses", 
            "artist": "Paul Cézanne", 
            "year": 2021, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image18.jpg"
            },
        {
            "title": "Yellow Blue Mélange", 
            "artist": "Henri de Toulouse-Lautrec", 
            "year": 2022, 
            "price":10000,
            "description":"Modern Art",
            "url":"static/images/image17.jpg"
            },
        {
            "title": "Spirit of the Dead Watching", 
            "artist": "Paul Gauguin,", 
            "year": 2020, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image16.jpg"
            },
        {
            "title": "The Scream", 
            "artist": "Edvard Munch", 
            "year": 2021, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image15.jpg"
            },
        {
            "title": "Paysage coloré", 
            "artist": "Jean Metzinger", 
            "year": 2022,
            "price":1000, 
            "description":"Modern Art",
            "url":"static/images/image14.jpg"},
        {
            "title": "I and the Village", 
            "artist": "Marc Chagall", 
            "year": 2023, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image13.jpg"},
        {
            "title": "Pere Tanguy ", 
            "artist": "Vincent van", 
            "year": 2020, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image12.jpg"},
        {
            "title": "Les Demoiselles ", 
            "artist": "Pablo Isaac", 
            "year": 2014, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image11.jpg"
            },
        {
            "title": "Cubismo Cubism", 
            "artist": "Roger Fresnaye", 
            "year": 2017,
            "price":1000, 
            "description":"Modern Art",
            "url":"static/images/image10.jpg"
            },
    
        {
            "title": "Figuren-Doppelpack", 
            "artist": "Alfio", 
            "year": 2014, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image7.jpg"
            },
        {
            "title": "Figuren Pack", 
            "artist": "Giuffrida", 
            "year": 2020, 
            "price":1000,
            "description":"Modern Art",
            "url":"static/images/image4.jpg"
            },
        {
            "title": "Knight Oil", 
            "artist": "Yuri", 
            "year": 2014, 
            "price":200,
            "description":"Modern Art",
            "url":"static/images/image3.jpg"
            },
        {
            "title": "Abstract Expressionism", 
            "artist": "Steve Johnson", 
            "year": 2020, 
            "price":200,
            "description":"Modern Art",
            "url":"static/images/image4.jpg"
            },
                    {
            "title": "Multi Colored Abstract ",
            "artist": "Zaksheuskaya", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel6.jpg"
            },
                    {
            "title": "Yellow Blue Abstract ",
            "artist": "Zaksheuskaya", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel1.jpg"
            },
                    {
            "title": "Blue Shade Abstract ",
            "artist": "Suzy Hazelwood", 
            "year": 2020,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel2.jpg"
            },
                    {
            "title": "Purple Blue Liquid Abstract ",
            "artist": "Anne Roenkae", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel3.jpg"
            },
        {
            "title": "Multi Colored Houses Abstract",
            "artist": "Lisa Fotios", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel4.jpg"
            },
        {
            "title": "Green Red Abstract ",
            "artist": "Nick Collins", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/carousel5.jpg"
            },
        {
            "title": "Pink Abstract ",
            "artist": "Nick", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/image9.jpg"
            },
            
    ]






if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    paintings = Painting.all()
    print("FOUND", len(paintings), "PAINTINGS:")
    if any(paintings):
        for painting in paintings:
        
            #breakpoint()
            pprint(dict(painting))
    else:
        #if input("Seed paintings? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    painting.seed()
        print("SEEDING RECORDS...")
        Painting.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    painting = painting.find(1)
    print(painting.title)

    print("------------")
    print("FILTERING RECORDS...")
    matches = painting.where(title="To Kill a Mockingbird")
    print(len(matches))
    painting = matches[0]
    print(painting.title)

    print("------------")
    print("CREATING NEW painting...")
    params = {
            "title": "Pink Abstract ",
            "artist": "Nick", 
            "year": 2022,
            "price":100,
            "description":"Modern Art", 
            "url":"static/images/image9.jpg"
    }
    painting.create(params)
