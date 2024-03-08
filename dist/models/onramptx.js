"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const sequelize_1 = require("sequelize");
const database_1 = __importDefault(require("../util/database"));
class OnRampTx extends sequelize_1.Model {
}
OnRampTx.init({
    id: {
        type: sequelize_1.DataTypes.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    token: sequelize_1.DataTypes.STRING,
    noOfTokens: sequelize_1.DataTypes.INTEGER,
    receiptAddress: sequelize_1.DataTypes.STRING,
    senderPhoneNumber: sequelize_1.DataTypes.STRING,
    amountToSend: sequelize_1.DataTypes.INTEGER,
    currency: sequelize_1.DataTypes.STRING,
    status: sequelize_1.DataTypes.BOOLEAN
}, {
    sequelize: database_1.default,
    modelName: 'OnRampTx'
});
exports.default = OnRampTx;
//# sourceMappingURL=onramptx.js.map