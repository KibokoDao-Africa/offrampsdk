import { Router } from 'express';
import * as controller from '../controllers/offrampController';

const router = Router();

// CRUD Routes /offramptx
router.get('/', controller.getOfframpTx); // /offramptx
router.get('/:offrampTxId', controller.getOfframpTxById); // /offramptx/:offrampTxId
router.post('/', controller.createOfframpTx); // /offramptx
router.put('/:offrampTxId', controller.updateOfframpTx); // /offramptx/:offrampTxId

export default router;
