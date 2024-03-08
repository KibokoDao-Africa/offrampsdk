import { Router } from 'express';
import * as controller from '../controllers/onrampController';

const router = Router();

// CRUD Routes /onramptx
router.get('/', controller.getOnRampTx); // /onramptx
router.get('/:onRampTxId', controller.getOnRampTxById); // /onramptx/:onRampTxId
router.post('/', controller.createOnRampTx); // /onramptx
router.put('/:onRampTxId', controller.updateOnRampTx); // /onramptx/:onRampTxId

export default router;
