"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.updateOfframpTx = exports.createOfframpTx = exports.getOfframpTxById = exports.getOfframpTx = void 0;
const offramptx_1 = __importDefault(require("../models/offramptx"));
// Get all OfframpTx
const getOfframpTx = async (req, res) => {
    try {
        const offramptx = await offramptx_1.default.findAll();
        res.status(200).json({ offramptx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.getOfframpTx = getOfframpTx;
// Get OfframpTx by ID
const getOfframpTxById = async (req, res) => {
    const offrampTxId = req.params.offrampTxId;
    try {
        const offrampTx = await offramptx_1.default.findByPk(offrampTxId);
        if (!offrampTx) {
            res.status(404).json({ message: 'OfframpTx not found!' });
            return;
        }
        res.status(200).json({ offrampTx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.getOfframpTxById = getOfframpTxById;
// Create OfframpTx
const createOfframpTx = async (req, res) => {
    const { token, noOfTokens, senderAddress, receiptPhoneNumber, amountToSend, currency, status } = req.body;
    try {
        const result = await offramptx_1.default.create({
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
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.createOfframpTx = createOfframpTx;
// Update OfframpTx
const updateOfframpTx = async (req, res) => {
    const offrampTxId = req.params.offrampTxId;
    const updatedAttributes = req.body;
    try {
        const offrampTx = await offramptx_1.default.findByPk(offrampTxId);
        if (!offrampTx) {
            res.status(404).json({ message: 'OfframpTx not found!' });
            return;
        }
        await offrampTx.update(updatedAttributes);
        res.status(200).json({ message: 'OfframpTx updated!', offrampTx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.updateOfframpTx = updateOfframpTx;
//# sourceMappingURL=offramp.js.map