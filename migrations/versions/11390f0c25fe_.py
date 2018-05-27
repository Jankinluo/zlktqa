"""empty message

Revision ID: 11390f0c25fe
Revises: ecf87fe01e9e
Create Date: 2018-04-19 17:10:58.705000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11390f0c25fe'
down_revision = 'ecf87fe01e9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'create_time')
    # ### end Alembic commands ###
