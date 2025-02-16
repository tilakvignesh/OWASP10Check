const express = require("express");
const jwt = require("jsonwebtoken");

const app = express();
app.use(express.json());

const SECRET_KEY = "weaksecret";

// Generate JWT
app.post("/login", (req, res) => {
    const { username } = req.body;
    
    const token = jwt.sign({ user: username, role: "user" }, SECRET_KEY, {
        algorithm: "HS256",
        expiresIn: "1h"
    });

    res.json({ token });
});

// Protected route
app.get("/admin", (req, res) => {
    const token = req.headers.authorization?.split(" ")[1];

    try {
        const decoded = jwt.decode(token, {complete: true})?.payload; // Insecure check
        console.log(decoded);
        
        if (decoded.role !== "admin") {
            return res.status(403).json({ message: "Access Denied" });
        }

        res.json({ message: "Welcome, Admin!" });
    } catch (err) {
        console.error(err);
        res.status(401).json({ message: "Invalid Token" });
    }
});

app.listen(3000, () => console.log("Server running on port 3000"));
