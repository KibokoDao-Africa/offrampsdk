import { DataTypes, Model } from 'sequelize';
import db from '../../util/database';

interface OnRampTxAttributes {
    id: number;
    token: string;
    noOfTokens: number;
    receiptAddress: string;
    senderPhoneNumber: string;
    amountToSend: number;
    currency: string;
    status: boolean;
}

class OnRampTx extends Model<OnRampTxAttributes> implements OnRampTxAttributes {
    public id!: number;
    public token!: string;
    public noOfTokens!: number;
    public receiptAddress!: string;
    public senderPhoneNumber!: string;
    public amountToSend!: number;
    public currency!: string;
    public status!: boolean;
}

OnRampTx.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    token: DataTypes.STRING,
    noOfTokens: DataTypes.INTEGER,
    receiptAddress: DataTypes.STRING,
    senderPhoneNumber: DataTypes.STRING,
    amountToSend: DataTypes.INTEGER,
    currency: DataTypes.STRING,
    status: DataTypes.BOOLEAN
}, {
    sequelize: db,
    modelName: 'OnRampTx'
});

export default OnRampTx;
