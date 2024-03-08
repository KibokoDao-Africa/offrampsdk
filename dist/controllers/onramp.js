"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.updateOnRampTx = exports.createOnRampTx = exports.getOnRampTxById = exports.getOnRampTx = void 0;
const onramptx_1 = __importDefault(require("../models/onramptx"));
// Get all OnRampTx
const getOnRampTx = async (req, res) => {
    try {
        const onramptx = await onramptx_1.default.findAll();
        res.status(200).json({ onramptx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.getOnRampTx = getOnRampTx;
// Get OnRampTx by ID
const getOnRampTxById = async (req, res) => {
    const onRampTxId = req.params.onRampTxId;
    try {
        const onRampTx = await onramptx_1.default.findByPk(onRampTxId);
        if (!onRampTx) {
            res.status(404).json({ message: 'OnRampTx not found!' });
            return;
        }
        res.status(200).json({ onRampTx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.getOnRampTxById = getOnRampTxById;
// Create OnRampTx
const createOnRampTx = async (req, res) => {
    const { token, noOfTokens, receiptAddress, senderPhoneNumber, amountToSend, currency, status } = req.body;
    try {
        const result = await onramptx_1.default.create({
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
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.createOnRampTx = createOnRampTx;
// Update OnRampTx
const updateOnRampTx = async (req, res) => {
    const onRampTxId = req.params.onRampTxId;
    const updatedAttributes = req.body;
    try {
        const onRampTx = await onramptx_1.default.findByPk(onRampTxId);
        if (!onRampTx) {
            res.status(404).json({ message: 'OnRampTx not found!' });
            return;
        }
        await onRampTx.update(updatedAttributes);
        res.status(200).json({ message: 'OnRampTx updated!', onRampTx });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
};
exports.updateOnRampTx = updateOnRampTx;
//# sourceMappingURL=onramp.js.map