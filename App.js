import React, { useState } from "react";
import axios from "axios";

function App() {
    const [file, setFile] = useState(null);
    const [token, setToken] = useState("");

    const uploadFile = async () => {
        const formData = new FormData();
        formData.append("file", file);

        const response = await axios.post("http://localhost:5000/upload", formData, {
            headers: {
                Authorization: "valid_token", // Replace with real token
            },
        });

        setToken(response.data.token);
    };

    return (
        <div>
            <h1>DataVault</h1>
            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
            />
            <button onClick={uploadFile}>Upload</button>
            {token && <p>Your file token: {token}</p>}
        </div>
    );
}

export default App;
