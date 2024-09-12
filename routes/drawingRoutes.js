const express = require('express');
const DrawingController = require('../controllers/drawingController');

const router = express.Router();

router.post('/', DrawingController.createDrawing);
router.get('/', DrawingController.getAllDrawings);
router.get('/:id', DrawingController.getDrawingById);
router.put('/:id', DrawingController.updateDrawing);
router.delete('/:id', DrawingController.deleteDrawing);

module.exports = router;
