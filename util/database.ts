import { Sequelize } from 'sequelize';

const sequelize = new Sequelize(
    process.env.PG_DB as string,
    process.env.PG_USER as string,
    process.env.PG_PASSWORD as string,
    {
        host: process.env.PG_HOST as string,
        dialect: 'postgres',
    }
);

export default sequelize;
