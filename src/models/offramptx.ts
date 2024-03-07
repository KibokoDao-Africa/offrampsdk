import { DataTypes, Model } from 'sequelize';
import db from '../util/database';

interface OfframpAttributes {
    id: number;
    token: string;
    noOfTokens: number;
    senderAddress: string;
    receiptPhoneNumber: string;
    amountToSend: number;
    currency: string;
    status: boolean;
}

class Offramp extends Model<OfframpAttributes> implements OfframpAttributes {
    public id!: number;
    public token!: string;
    public noOfTokens!: number;
    public senderAddress!: string;
    public receiptPhoneNumber!: string;
    public amountToSend!: number;
    public currency!: string;
    public status!: boolean;
}

Offramp.init({
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
    modelName: 'Offramp'
});

export default Offramp;
