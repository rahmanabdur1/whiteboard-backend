const Drawing = require('../models/Drawing');

class DrawingController {
    async createDrawing(req, res) {
        try {
            const drawing = new Drawing(req.body);
            await drawing.save();
            res.status(201).send(drawing);
        } catch (error) {
            console.error('Error creating drawing:', error);
            res.status(400).send({ error: 'Unable to create drawing' });
        }
    }

    async getAllDrawings(req, res) {
        try {
            const drawings = await Drawing.find();
            res.status(200).send(drawings);
        } catch (error) {
            console.error('Error fetching drawings:', error);
            res.status(500).send({ error: 'Unable to fetch drawings' });
        }
    }

    async getDrawingById(req, res) {
        try {
            const drawing = await Drawing.findById(req.params.id);
      
            if (!drawing) return res.status(404).send({ error: 'Drawing not found' });
            res.status(200).send(drawing);
        } catch (error) {
            console.error('Error fetching drawing:', error);
            res.status(500).send({ error: 'Unable to fetch drawing' });
        }
    }

    async updateDrawing(req, res) {
        try {
            const drawing = await Drawing.findByIdAndUpdate(req.params.id, req.body, { new: true });
            if (!drawing) return res.status(404).send({ error: 'Drawing not found' });
            res.status(200).send(drawing);
        } catch (error) {
            console.error('Error updating drawing:', error);
            res.status(400).send({ error: 'Unable to update drawing' });
        }
    }

    async deleteDrawing(req, res) {
        try {
            const drawing = await Drawing.findByIdAndDelete(req.params.id);
            if (!drawing) return res.status(404).send({ error: 'Drawing not found' });
            res.status(200).send({ message: 'Drawing deleted' });
        } catch (error) {
            console.error('Error deleting drawing:', error);
            res.status(500).send({ error: 'Unable to delete drawing' });
        }
    }
}

module.exports = new DrawingController();
