"""Change some columns size

Revision ID: a849c7073f8
Revises: 4db99a451791
Create Date: 2016-06-23 16:46:05.958126

"""

# revision identifiers, used by Alembic.
revision = 'a849c7073f8'
down_revision = '4db99a451791'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('core_device', 'reference',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.Unicode(length=30),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('core_device', 'reference',
               existing_type=sa.Unicode(length=30),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)
    ### end Alembic commands ###
