"""empty message

Revision ID: 8126e8cfa95d
Revises: b581e83aa67b
Create Date: 2024-05-25 15:29:56.112531

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8126e8cfa95d'
down_revision = 'b581e83aa67b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tarefa', schema=None) as batch_op:
        batch_op.alter_column('projeto_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tarefa', schema=None) as batch_op:
        batch_op.alter_column('projeto_id',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
