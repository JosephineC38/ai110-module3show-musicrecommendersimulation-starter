# 🎧 Model Card: Music Recommender Simulation

## 1. Chill Lofi Beats to Find (& More) 

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
It is designed to find similar songs based on a profile (like Chill Lofi or Intense Rock). These songs are suggested based on many weighted factors, including energy fit, similar genres, right mood, and texture match. It ranks the songs based on the score from 1 to 7. It assumes that the user is only looking for one type of recommendation and can't mix recommendations. For example, you can't mix pop and metal, even if the user wants both. It is intended for classroom exploration because it doesn't use any actual real songs and isn't based off any lyrics.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
It gives each song a score from 1 to 7. User preferences considered are the user's favorite genre, energy, mood, and acoustics. For genre, it grants 2 points for the same genre and 1 point for the same genre family (e.g. jazz and lofi). The same logic applies for mood. For energy, up to 2 points can be given based on how close the energy is to the user's preference. The same logic applies to acoustics, but only a max of 1 poin can be given. It adds all these factors up for a final score, the higher the better. At first, the starter logic had no real function, so I added the scoring system so users can find the best songs based on ranking. 

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
There are 17 songs in the catalog and I added 7 songs from the original. The genres represented are pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop, classical, edm, reggie, metal, country, and r&b. FOr moods, there are happy, chill, intense, relaxed, moody, focused, confident, melancholic, euphoric, laid-back, aggressive, nostalgic, and romantic. There are many parts of musical taste missing as I don't have every genre and mood there. Futhermore, I didn't account for song length, lyrics, lyric language, and many other factors.


## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
It works well identifying similar genres and mood as giving a higher score. For example, when I listen to lofi, there's a lot of clssical music mixed in. Additonally, my idea of a quiet, calming cafe is one where jazz music plays, which fits the overall vibe and intuition of lofi. It also correctly sorts moods into similar categories like chill and focused, which are words I would use to describe a lofi playlist. 

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---
Since the system has no memory of what songs the user has previously played, it can't suggest better songs. For example, if the user hates a certain lofi artist while having a lofi profile, the system has no way of knowing. It's worse if that lofi artist is popular, as the system will keep recommending it regardless. It also can't learn the taste of users and
what style of lofi they might prefer like ones with cacthy or sad lyrics. 


## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
I tested the user profiles of High-Energy Pop, Chill Lofi, and Deep Intense Rock. I was mainly looking for repeating songs between the profiles as they were pretty different. The only songs in common were Sunrise City between High-Energy Pop and Intense Rock, althought they had different rankings. What surpised me was how low the scores were for Deep Intense Rock compared to the other two profiles, which never went below a 3. I compared the differences in energy and mood between the profiles.
As for the profiles themseleves, High-Energy Pop prefers the pop genre with a higher energy and a happy mood. Chill Lofi likes the genres lofi, jazz, and ambient combined with a lower energy and a more chill mood. Deep Intense Rock wants the genres rock and metal with a higher energy and more intense mood.  

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
I would want it to handle more complex user tastes, like if a user wants both classical and rock songs. Some songs might have a mixture of both that my system can't properly find now. Some additional features that I want to add are recommending based on what's popular and finding more indie gems based on the user's preferences.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

---
I learned that recommender systems are a lot more complicated than I thought and I wonder out of what number are songs ranked based in actual systems. Something unexpected was the filtering system as I didn't know that many companies use two different types of filtering, I thought it was only one type. It has also caused me to think more about how lyrics and popular artists may play a role in music recs. It hasn't really changed the way I think about then as I don't use many music recommendation apps, so I don't have a base on if the songs suggested are accurate or not. However, it has caused me to wonder how accurate the current apps are and why.

My biggest learning moment was creating a scoring system that had to consider the weight of each factor. WHat mattered the most when recommending a song? AI tools helped me create the basis of the scoring system as well as creating the genre and mood groups.
It surprises me that simple algorithms can somewhat feel like recommendations and suggest good songs. It's werid to think that my music taste can be predicated, but I'm unsure it it really can. I might like metal but I'm also a fan of lofi, two genres very diferent from each other. If I were to try again, I would want to add mixed user preferences first, to better reflect a person's music taste. 