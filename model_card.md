# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

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

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

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

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
