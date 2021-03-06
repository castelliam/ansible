# (c) 2012-2015, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.compat.tests import unittest
from ansible.plugins.cache.base import BaseCacheModule
from ansible.plugins.cache.memcached import CacheModule as MemcachedCache
from ansible.plugins.cache.memory import CacheModule as MemoryCache
from ansible.plugins.cache.redis import CacheModule as RedisCache


class TestAbstractClass(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_subclass_error(self):
        class CacheModule1(BaseCacheModule):
                pass
        with self.assertRaises(TypeError):
            CacheModule1()

        class CacheModule2(BaseCacheModule):
            def get(self, key):
                super(CacheModule2, self).get(key)

        with self.assertRaises(TypeError):
            CacheModule2()

    def test_subclass_success(self):
        class CacheModule3(BaseCacheModule):
            def get(self, key):
                super(CacheModule3, self).get(key)

            def set(self, key, value):
                super(CacheModule3, self).set(key, value)

            def keys(self):
                super(CacheModule3, self).keys()

            def contains(self, key):
                super(CacheModule3, self).contains(key)

            def delete(self, key):
                super(CacheModule3, self).delete(key)

            def flush(self):
                super(CacheModule3, self).flush()

            def copy(self):
                super(CacheModule3, self).copy()

        self.assertIsInstance(CacheModule3(), CacheModule3)

    def test_memcached_cachemodule(self):
        self.assertIsInstance(MemcachedCache(), MemcachedCache)

    def test_memory_cachemodule(self):
        self.assertIsInstance(MemoryCache(), MemoryCache)

    def test_redis_cachemodule(self):
        self.assertIsInstance(RedisCache(), RedisCache)
