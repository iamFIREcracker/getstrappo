"""add user email

Revision ID: 353e2e032af5
Revises: 3d42535a0449
Create Date: 2014-06-16 00:20:24.169262

"""

# revision identifiers, used by Alembic.
revision = '353e2e032af5'
down_revision = '3d42535a0449'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    ### end Alembic commands ###
