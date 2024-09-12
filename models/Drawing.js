const mongoose = require('mongoose');

const drawingSchema = new mongoose.Schema({
    title: { type: String, required: true },
    elements: [
        {
            type: { type: String, enum: ['line', 'shape', 'text'], required: true },
            properties: {
                x: { type: Number, required: true },
                y: { type: Number, required: true },
                width: { type: Number },
                height: { type: Number },
                color: { type: String },
                text: { type: String }
            }
        }
    ]
});

module.exports = mongoose.model('Drawing', drawingSchema);
