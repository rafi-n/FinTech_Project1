create database if not exists ditiae;

\c ditiae;

drop table if exists ticker;

create table ticker (
    row_id bigserial primary key,
    timestamp timestamp with time zone,
    open double precision not null,
    high double precision not null,
    low double precision not null,
    close double precision not null,
    volume bigint not null,
    trade_count bigint not null,
    vwap double precision not null,
    symbol varchar(16) not null,
    asset_class varchar(10) not null,
    unique (timestamp, asset_class, symbol)
    );
