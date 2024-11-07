# app/models/category.py

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base
#
# # Таблица-связка между продуктами и категориями.
# product_category_association = Table(
#     'product_category_association',
#     Base.metadata,
#     Column('product_id', UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True),
#     Column('category_id', UUID(as_uuid=True), ForeignKey('categories.id'), primary_key=True)
# )
#
# # Таблица-связка между продуктами и характеристиками.
# product_characteristic_association = Table(
#     'product_characteristic_association',
#     Base.metadata,
#     Column('product_id', UUID(as_uuid=True), ForeignKey('products.id')),
#     Column('characteristic_id', UUID(as_uuid=True), ForeignKey('characteristics.id'))
# )
#
# # Таблица-связка между вариантами и характеристиками.
# variant_characteristic_association = Table(
#     'variant_characteristic_association',
#     Base.metadata,
#     Column('variant_id', UUID(as_uuid=True), ForeignKey('product_variants.id')),
#     Column('characteristic_id', UUID(as_uuid=True), ForeignKey('characteristics.id'))
# )
