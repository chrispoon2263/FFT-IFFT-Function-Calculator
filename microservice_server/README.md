# Randomizer Microservice

- This microservice provides allows users to generate randomized inputs by clicking a button on the host UI. The backend updates and logs the randomized values in real-time.

--- 

### Installation & Setup

```python
# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Install dependencies
pip3 install -r requirements.txt

# 4. Start the microservice in a new terminal
python3 microservice_server.py
```
---
### Usage
- Open a web browser and go to http://localhost:63861/
- Click the “Random” button on the host UI to randomly pick two new input functions
- Observe the command line updating with new randomized values on every click

---
![alt text](images/randomizer.png)
