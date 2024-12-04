# DataVault  

**DataVault** is a secure, encrypted, and decentralized file storage and sharing system. It enables users to upload files, encrypt them locally, and share access securely using unique access tokens. Perfect for individuals and teams who need secure file handling without relying on centralized solutions.  

---

## Features  
- **End-to-End Encryption**: Files are encrypted on the client side before uploading.  
- **Decentralized Storage**: Files are distributed across nodes or a custom system.  
- **Secure Access Tokens**: Share files with unique, time-limited access tokens.  
- **File Versioning**: Maintain a history of changes to files.  
- **User Authentication**: Simple and secure login using JWT (JSON Web Token).  
- **Cross-Platform**: Access via web, desktop, or mobile app.  

---

## Getting Started  

### Prerequisites  
- **Node.js**  
- **Python 3.x**  
- **MongoDB**  

### Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/FITIMDOTORG/datavault.git


Navigate to the project directory:
-cd datavault


## Install backend dependencies:
- pip install -r backend/requirements.txt

##Install frontend dependencies:
- cd frontend
- npm install

##Start the backend server:
- cd backend
- python app.py


##Start the frontend server:
-cd frontend
- npm start

Open the app in your browser:
http://localhost:3000



##Folder Structure


datavault/
├── backend/
│   ├── app.py           # Main backend logic
│   ├── auth.py          # Authentication module
│   ├── storage.py       # File storage handler
│   ├── requirements.txt # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   ├── components/  # React components
│   │   ├── services/    # API services
│   │   ├── styles/      # CSS files
│   ├── public/
│   ├── package.json     # Frontend dependencies
│   ├── index.html       # Frontend entry point
├── README.md
├── LICENSE              # License information
├── .gitignore           # Ignored files for Git



## Roadmap
 - [X] File Upload: Basic upload functionality with token generation.
 - [X] Token-Based File Access: Securely fetch files using access tokens.
 - End-to-End Encryption: Encrypt files on the client side.
 - Decentralized Storage: Integrate with IPFS or a custom node system.
 - Authentication: Full user login with JWT.
 - File Versioning: Maintain a history of changes to files.


## Contributing
We welcome contributions! To get started:

## Fork the repository.
Create a new branch for your feature or bugfix:

## git checkout -b feature-name
Commit your changes:

## git commit -m "Add new feature"
Push to your branch:

## git push origin feature-name
Open a pull request on GitHub.
   
