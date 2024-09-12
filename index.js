const express = require('express');
const dotenv = require("dotenv");
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors'); 
const drawingRoutes = require('./routes/drawingRoutes');
const PORT = process.env.PORT || 5000;
// Load environment variables
dotenv.config();

const app = express();

// Middleware
app.use(cors());  // Enable CORS
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB, {  
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// API Routes
app.use('/api/drawings', drawingRoutes);

// Start server
app.get('/', (req, res)=>{
    res.send('server running')
})

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
