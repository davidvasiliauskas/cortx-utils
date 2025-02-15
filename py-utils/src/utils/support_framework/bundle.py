#!/usr/bin/env python3

# CORTX-Py-Utils: CORTX Python common library.
# Copyright (c) 2021 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.


class Bundle:
    def __init__(self, bundle_id, bundle_path, is_shared, comment):
        """Initialiases bundle object, which will have support bundle information."""
        self._bundle_id = bundle_id
        self._bundle_path = bundle_path
        self._comment = comment
        self._is_shared = is_shared

    @property
    def bundle_id(self):
        return self._bundle_id

    @property
    def bundle_path(self):
        return self._bundle_path

    @property
    def is_shared(self):
        return self._is_shared

    @property
    def comment(self):
        return self._comment
