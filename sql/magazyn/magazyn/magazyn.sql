DROP TABLE IF EXISTS dane_customers;
CREATE TABLE dane_customers
(
    customer_id	INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    address TEXT
);

DROP TABLE IF EXISTS dane_orders;
CREATE TABLE dane_orders
(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    subscription_id	INTEGER,
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES dane_customers(customer_id)
    FOREIGN KEY (subscription_id) REFERENCES dane_subscriptions(subscription_id)
);

DROP TABLE IF EXISTS dane_subscriptions;
CREATE TABLE dane_subscriptions
(
    subscription_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_month DECIMAL,
    subscription_length	TEXT
);
