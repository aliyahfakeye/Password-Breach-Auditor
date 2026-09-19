## HAVE I BEEN PWNED?

This is a program designed to check how many times a given password has appeared in known breaches.

A lot of people use passwords that are easy to remember (e.g. their birthday, their favourite colour or food, their dog's name, or ABCD1234...). 

However, what they don't realise is those easy to remember passwords are also easy to crack passwords for hackers. This gives hackers a bigger chance of being able to break into your personal accounts and use sensitive information for malicious purposes.

Hence, this program will allow you to check how many times a given password has appeared in a known breach.

## Key Features & Security Design
- **$k$-Anonymity Implementation:** The application computes a 160-bit SHA-1 digest of the input locally and queries the Have I Been Pwned (HIBP) Range API using only a 5-character prefix. 
- **Zero-Knowledge Privacy:** The remaining 35 characters (suffix) are matched locally on the client machine, ensuring the user's password never leaves memory in transit.
- **Robust Error Handling:** Validates HTTP responses and handles API status codes gracefully.

## Tech Stack
- **Python 3**
- **Libraries:** `hashlib` (standard library), `requests`

## Getting Started

### Prerequisites
- Python 3.8+
- `pip install requests`

### Running the App
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/password-breach-checker.git](https://github.com/your-username/password-breach-checker.git)
   cd password-breach-checker

2. Run the script:
    python main.py
