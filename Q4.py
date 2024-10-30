from sqlalchemy import create_engine, and_, cast, Date
from sqlalchemy.orm import aliased, sessionmaker
from sqlalchemy.sql import select
from your_models import CPIU, Product, ProductDetail, Client  # Import your ORM models

'''
select c.pretty_name, pd.product_brand, p.ndc11, p.product_name, cp.period, cp.cpiu 
from md.cpiu cp
left join md.product p on p.id = cp.sb_id and p.status = 'ACTIVE'
right join md.product_detail pd on pd.product_id = p.id and pd.status = 'ACTIVE'
join md.client c on c.id = p.client_id  and c.id = pd.client_id
where c.pretty_name = 'Aquestive Therapeutics, Inc' and p.ndc11 = '10094022060' and cp.status = 'ACTIVE' and cp.period = '202305'
and cp.start_date <= cast('2023-04-01' as date) and cp.end_date >= cast('2023-04-30' as date)'''


# Initialize database connection (update with actual database URI)
engine = create_engine("your_database_uri")
Session = sessionmaker(bind=engine)
session = Session()

# Aliasing the tables for cleaner references
cpiu_alias = aliased(CPIU)
product_alias = aliased(Product)
product_detail_alias = aliased(ProductDetail)
client_alias = aliased(Client)

# Build query with joins and filters
query = (
    session.query(
        client_alias.pretty_name,
        product_detail_alias.product_brand,
        product_alias.ndc11,
        product_alias.product_name,
        cpiu_alias.period,
        cpiu_alias.cpiu
    )
    .select_from(cpiu_alias)
    .join(product_alias, 
          and_(
              product_alias.id == cpiu_alias.sb_id,
              product_alias.status == 'ACTIVE'
          ), isouter=True)  
    .join(product_detail_alias, 
          and_(
              product_detail_alias.product_id == product_alias.id,
              product_detail_alias.status == 'ACTIVE'
          ), isouter=False)  # RIGHT JOIN simulated
    .join(client_alias, 
          and_(
              client_alias.id == product_alias.client_id,
              client_alias.id == product_detail_alias.client_id
          ))
    .filter(
        client_alias.pretty_name == 'Aquestive Therapeutics, Inc',
        product_alias.ndc11 == '10094022060',
        cpiu_alias.status == 'ACTIVE',
        cpiu_alias.period == '202305',
        cpiu_alias.start_date <= cast('2023-04-01', Date),
        cpiu_alias.end_date >= cast('2023-04-30', Date)
    )
)

results = query.all()
for row in results:
    print(row)
