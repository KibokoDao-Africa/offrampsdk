import { Request, Response } from 'express';
import OfframpTx from '../models/offramptx';

// Get all OfframpTx
export const getOfframpTx = async (req: Request, res: Response): Promise<void> => {
    try {
        const offramptx = await OfframpTx.findAll();
        res.status(200).json({ offramptx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Get OfframpTx by ID
export const getOfframpTxById = async (req: Request, res: Response): Promise<void> => {
    const offrampTxId: string = req.params.offrampTxId;
    try {
        const offrampTx = await OfframpTx.findByPk(offrampTxId);
        if (!offrampTx) {
            res.status(404).json({ message: 'OfframpTx not found!' });
            return;
        }
        res.status(200).json({ offrampTx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Create OfframpTx
export const createOfframpTx = async (req: Request, res: Response): Promise<void> => {
    const { token, noOfTokens, senderAddress, receiptPhoneNumber, amountToSend, currency, status } = req.body;
    try {
        const result = await OfframpTx.create({
            token,
            noOfTokens,
            senderAddress,
            receiptPhoneNumber,
            amountToSend,
            currency,
            status
        });
        console.log('Created OfframpTx');
        res.status(201).json({
            message: 'OfframpTx created successfully!',
            offrampTx: result
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Update OfframpTx
export const updateOfframpTx = async (req: Request, res: Response): Promise<void> => {
    const offrampTxId: string = req.params.offrampTxId;
    const updatedAttributes = req.body;
    try {
        const offrampTx = await OfframpTx.findByPk(offrampTxId);
        if (!offrampTx) {
            res.status(404).json({ message: 'OfframpTx not found!' });
            return;
        }
        await offrampTx.update(updatedAttributes);
        res.status(200).json({ message: 'OfframpTx updated!', offrampTx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}
