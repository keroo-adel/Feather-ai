import requests

def generate_keywrods(topic):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': 'for this topic genrate keywrods sprated by , \n topic : {} '.format(topic),
        },
        headers={'api-key': '4a4c76a8-df35-4832-818b-b9997a886416'}
    )
    
    return r.json()

def generate_ideas(topic,keywords):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': """genreate articles ideas based on this keywords and this topic name
                        topic : {}
                        keywords : {} 
                        by this form idea1, idea2 , ....etc without number
                        """.format(topic,keywords),
        },
        headers={'api-key': '4a4c76a8-df35-4832-818b-b9997a886416'}
    )
    
    return r.json()

def generate_outlines(topic,keywords):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': """genreate articles outlines only based on this keywords and this topic name 
                        topic : {}
                        keywords : {} 
                        by this 
                        I. outline 1 
                        A. sub outline 1
                        B. sub outline 2
                        
                        II. outline 2
                        A. sub outline 1
                        B. sub outline 2
                        
                        ..... etc 
                        """.format(topic,keywords),
        },
        headers={'api-key': '4a4c76a8-df35-4832-818b-b9997a886416'}
    )
    
    return r.json()

def generate_article(outlines_suboutlines):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': """write article text for every outline this outlines : 
                    {}
                    write above every sub outline its titlte 
                        
                    """.format(outlines_suboutlines),
        },
        headers={'api-key': '4a4c76a8-df35-4832-818b-b9997a886416'}
    )
    
    return r.json()

print(generate_keywrods("messi"))
















