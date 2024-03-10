import { Router } from 'express';
import * as offrampController from '../controllers/offrampController';

const router = Router();

// CRUD Routes /offramptx
router.get('/', offrampController.getOfframpTx); // /offramptx
router.get('/:offrampTxId', offrampController.getOfframpTxById); // /offramptx/:offrampTxId
router.post('/', offrampController.createOfframpTx); // /offramptx
router.put('/:offrampTxId', offrampController.updateOfframpTx); // /offramptx/:offrampTxId

export default router;
