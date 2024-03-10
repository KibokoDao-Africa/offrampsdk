import { Router } from 'express';

import * as onrampController from '../controllers/onrampController';



const router = Router();

// CRUD Routes /onramptx
router.get('/', onrampController.getOnRampTx); // /onramptx
router.get('/:onRampTxId', onrampController.getOnRampTxById); // /onramptx/:onRampTxId
router.post('/', onrampController.createOnRampTx); // /onramptx
router.put('/:onRampTxId', onrampController.updateOnRampTx); // /onramptx/:onRampTxId

export default router;
