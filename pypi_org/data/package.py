import datetime
from typing import List

import sqlalchemy.orm as orm
import sqlalchemy as sa

from pypi_org.data.modelbase import SqlAlchemyBase
from pypi_org.data.releases import Release


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String, index=True)
    author_email = sa.Column(sa.String, index=True)

    licence = sa.Column(sa.String)

    # release relationship
    releases: List[Release] = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    def __repr__(self):
        return '<Package {}>'.format(self.id)


p = Package()
print(p.id)
print("All releases")
for r in p.releases:
    print("{}.{}.{}".format(r.major_ver,r.minor_ver,r.build_ver))