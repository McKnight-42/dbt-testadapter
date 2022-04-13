from dbt.adapters.testadapter.connections import TestAdapterConnectionManager
from dbt.adapters.testadapter.connections import TestAdapterCredentials
from dbt.adapters.testadapter.impl import TestAdapterAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import testadapter


Plugin = AdapterPlugin(
    adapter=TestAdapterAdapter,
    credentials=TestAdapterCredentials,
    include_path=testadapter.PACKAGE_PATH,
)
