# Randomizer Microservice

- This microservice provides a simple UI that allows users to generate randomized inputs by clicking a button. The backend updates and logs the randomized values in real-time.

--- 

### Installation & Setup

```python
# 1. Create a virtual environment
python3 -m venv venv

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Install dependencies
pip3 install -r requirements.txt

# 4. Start the microservice
python3 microservice_server.py
```
---
### Usage
- Open a web browser and go to http://localhost:63861/
- Click the “Random” button on the UI
- Observe the command line updating with new randomized values on every click
