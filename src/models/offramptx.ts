import { DataTypes, Model } from 'sequelize';
import db from '../util/database';

interface OfframpTxAttributes {
    id: number;
    token: string;
    noOfTokens: number;
    senderAddress: string;
    receiptPhoneNumber: string;
    amountToSend: number;
    currency: string;
    status: boolean;
}

class OfframpTx extends Model<OfframpTxAttributes> implements OfframpTxAttributes {
    public id!: number;
    public token!: string;
    public noOfTokens!: number;
    public senderAddress!: string;
    public receiptPhoneNumber!: string;
    public amountToSend!: number;
    public currency!: string;
    public status!: boolean;
}

OfframpTx.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    token: DataTypes.STRING,
    noOfTokens: DataTypes.INTEGER,
    senderAddress: DataTypes.STRING,
    receiptPhoneNumber: DataTypes.STRING,
    amountToSend: DataTypes.INTEGER,
    currency: DataTypes.STRING,
    status: DataTypes.BOOLEAN
}, {
    sequelize: db,
    modelName: 'OfframpTx'
});

export default OfframpTx;
