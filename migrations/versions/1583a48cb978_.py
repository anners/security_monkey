"""Adding Unique Index to TechName and AccountName

Revision ID: 1583a48cb978
Revises: c93f246859f7
Create Date: 2017-03-16 14:01:37.463000

"""

# revision identifiers, used by Alembic.
revision = '1583a48cb978'
down_revision = 'c93f246859f7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_account_name', 'account', ['name'], unique=True)
    op.drop_constraint(u'account_name_uc', 'account', type_='unique')
    op.create_index('ix_technology_name', 'technology', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_technology_name', table_name='technology')
    op.create_unique_constraint(u'account_name_uc', 'account', ['name'])
    op.drop_index('ix_account_name', table_name='account')
    # ### end Alembic commands ###
