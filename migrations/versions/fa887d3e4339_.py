"""empty message

Revision ID: fa887d3e4339
Revises: 6aa7cbeb79bf
Create Date: 2021-05-16 18:59:42.117794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa887d3e4339'
down_revision = '6aa7cbeb79bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String()))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), nullable=False))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
