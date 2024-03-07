import { Request, Response } from 'express';
import OnRampTx from '../models/onramptx';

// Get all OnRampTx
export const getOnRampTx = async (req: Request, res: Response): Promise<void> => {
    try {
        const onramptx = await OnRampTx.findAll();
        res.status(200).json({ onramptx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Get OnRampTx by ID
export const getOnRampTxById = async (req: Request, res: Response): Promise<void> => {
    const onRampTxId: string = req.params.onRampTxId;
    try {
        const onRampTx = await OnRampTx.findByPk(onRampTxId);
        if (!onRampTx) {
            res.status(404).json({ message: 'OnRampTx not found!' });
            return;
        }
        res.status(200).json({ onRampTx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Create OnRampTx
export const createOnRampTx = async (req: Request, res: Response): Promise<void> => {
    const { token, noOfTokens, receiptAddress, senderPhoneNumber, amountToSend, currency, status } = req.body;
    try {
        const result = await OnRampTx.create({
            token,
            noOfTokens,
            receiptAddress,
            senderPhoneNumber,
            amountToSend,
            currency,
            status
        });
        console.log('Created OnRampTx');
        res.status(201).json({
            message: 'OnRampTx created successfully!',
            onRampTx: result
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Update OnRampTx
export const updateOnRampTx = async (req: Request, res: Response): Promise<void> => {
    const onRampTxId: string = req.params.onRampTxId;
    const updatedAttributes = req.body;
    try {
        const onRampTx = await OnRampTx.findByPk(onRampTxId);
        if (!onRampTx) {
            res.status(404).json({ message: 'OnRampTx not found!' });
            return;
        }
        await onRampTx.update(updatedAttributes);
        res.status(200).json({ message: 'OnRampTx updated!', onRampTx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
}
