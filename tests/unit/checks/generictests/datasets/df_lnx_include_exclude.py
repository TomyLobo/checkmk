#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
from cmk.base.plugins.agent_based.df_section import parse_df
from cmk.base.plugins.agent_based.utils.df import FILESYSTEM_DEFAULT_PARAMS

checkname = 'df'

parsed = parse_df([
    ['tmpfs', 'tmpfs', '1620324', '2320', '1618004', '1%', '/run'],
    ['/dev/mapper/ubuntu--vg-root', 'ext4', '242791844', '59957024', '170431928', '27%', '/'],
    ['tmpfs', 'tmpfs', '8101604', '226244', '7875360', '3%', '/dev/shm'],
    ['tmpfs', 'tmpfs', '5120', '4', '5116', '1%', '/run/lock'],
    ['tmpfs', 'tmpfs', '8101604', '0', '8101604', '0%', '/sys/fs/cgroup'],
    ['/dev/nvme0n1p2', 'ext4', '721392', '294244', '374684', '44%', '/boot'],
    ['/dev/nvme0n1p1', 'vfat', '523248', '31468', '491780', '7%', '/boot/efi'],
    ['tmpfs', 'tmpfs', '1620320', '68', '1620252', '1%', '/run/user/1000'],
    ['tmpfs', 'tmpfs', '8101604', '8612', '8092992', '1%', '/opt/omd/sites/netapp/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6360', '8095244', '1%', '/opt/omd/sites/heute/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6460', '8095144', '1%', '/opt/omd/sites/site1/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6456', '8095148', '1%', '/opt/omd/sites/site2/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6484', '8095120', '1%', '/opt/omd/sites/site3/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6476', '8095128', '1%', '/opt/omd/sites/site4/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6404', '8095200', '1%', '/opt/omd/sites/site5/tmp'],
    ['tmpfs', 'tmpfs', '8101604', '6388', '8095216', '1%', '/opt/omd/sites/site10/tmp'],
    ['[df_inodes_start]'],
    ['tmpfs', 'tmpfs', '2025401', '1287', '2024114', '1%', '/run'],
    ['/dev/mapper/ubuntu--vg-root', 'ext4', '15491072', '1266406', '14224666', '9%', '/'],
    ['tmpfs', 'tmpfs', '2025401', '120', '2025281', '1%', '/dev/shm'],
    ['tmpfs', 'tmpfs', '2025401', '7', '2025394', '1%', '/run/lock'],
    ['tmpfs', 'tmpfs', '2025401', '18', '2025383', '1%', '/sys/fs/cgroup'],
    ['/dev/nvme0n1p2', 'ext4', '46848', '321', '46527', '1%', '/boot'],
    ['/dev/nvme0n1p1', 'vfat', '0', '0', '0', '-', '/boot/efi'],
    ['tmpfs', 'tmpfs', '2025401', '105', '2025296', '1%', '/run/user/1000'],
    ['tmpfs', 'tmpfs', '2025401', '1547', '2023854', '1%', '/opt/omd/sites/netapp/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1531', '2023870', '1%', '/opt/omd/sites/heute/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1541', '2023860', '1%', '/opt/omd/sites/site1/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1541', '2023860', '1%', '/opt/omd/sites/site2/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1541', '2023860', '1%', '/opt/omd/sites/site3/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1541', '2023860', '1%', '/opt/omd/sites/site4/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1541', '2023860', '1%', '/opt/omd/sites/site5/tmp'],
    ['tmpfs', 'tmpfs', '2025401', '1536', '2023865', '1%', '/opt/omd/sites/site10/tmp'],
    ['[df_inodes_end]'],
])

mock_host_conf_merged = {
    '': {
        'ignore_fs_types': ['tmpfs', 'nfs', 'smbfs', 'cifs', 'iso9660'],
        'never_ignore_mountpoints': ['~.*/omd/sites/[^/]+/tmp$'],
        "groups": [
            {
                'group_name': 'group1',
                'patterns_include': ['/opt/omd/sites/*'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group2',
                'patterns_include': ['/opt/omd/sites/site[12]/*'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group2',
                'patterns_include': ['/opt/omd/sites/site[3]/*'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group3',
                'patterns_include': ['*'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group4',
                'patterns_include': ['/opt/omd/sites/*'],
                'patterns_exclude': ['/opt/omd/sites/site[2,4]/*']
            },
            {
                'group_name': 'group5',
                'patterns_include': ['/opt/omd/sites/site1*'],
                'patterns_exclude': ['/opt/omd/sites/site10/*']
            },
            {
                'group_name': 'group5',
                'patterns_include': [''],
                'patterns_exclude': ['']
            },
            {
                'group_name': 'group_empty_1',
                'patterns_include': [''],
                'patterns_exclude': []
            },
            {
                'group_name': 'group_empty_2',
                'patterns_include': ['/notfound'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group_empty_3',
                'patterns_include': [],
                'patterns_exclude': ['*']
            },
            {
                'group_name': 'group_empty_4',
                'patterns_include': ['*'],
                'patterns_exclude': []
            },
            {
                'group_name': 'group_empty_4',
                'patterns_include': [],
                'patterns_exclude': ['*']
            },
            {
                'group_name': 'group_empty_5',
                'patterns_include': [],
                'patterns_exclude': []
            },
        ]
    }
}

discovery = {
    '': [
        (
            'group1',
            {
                'patterns': (['/opt/omd/sites/*'], []),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
        (
            'group2',
            {
                'patterns': (['/opt/omd/sites/site[12]/*', '/opt/omd/sites/site[3]/*'], []),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
        (
            'group3',
            {
                'patterns': (['*'], []),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
        (
            'group4',
            {
                'patterns': (['/opt/omd/sites/*'], ['/opt/omd/sites/site[2,4]/*']),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
        (
            'group5',
            {
                'patterns': (['/opt/omd/sites/site1*', ''], ['/opt/omd/sites/site10/*', '']),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
                "mountpoint_for_block_devices": "volume_name",
            },
        ),
    ],
}

checks = {
    '': [
        (
            'group1',
            {
                **FILESYSTEM_DEFAULT_PARAMS,
                'patterns': (['/opt/omd/sites/*'], []),
                'grouping_behaviour': 'mountpoint',
                "item_appearance": "mountpoint",
            },
            [
                (0, 'Used: 0.08% - 52.4 MiB of 61.8 GiB', [('fs_used', 52.3828125, 50635.025,
                                                           56964.403125, 0, None),
                                                          ('fs_free', 63241.3984375, None, None, 0, None),
                                                          ('fs_used_percent', 0.0827613889792688, 80.0, 90.0, 0.0, 100.0),
                                                          ('fs_size', 63293.78125, None, None, 0, None)]),
                (0, '', [('inodes_used', 12319, 14582887.200000001, 15393047.6, 0.0, 16203208.0)]),
                (0, '8 filesystems', []),
            ],
        ),
        ('group2', {
            **FILESYSTEM_DEFAULT_PARAMS,
            'patterns': (['/opt/omd/sites/site[12]/*', '/opt/omd/sites/site[3]/*'], []),
            'grouping_behaviour': 'mountpoint',
            "item_appearance": "mountpoint",
        }, [
            (0, 'Used: 0.08% - 18.9 MiB of 23.2 GiB', [('fs_used', 18.9453125, 18988.134375,
                                                       21361.651171875, 0, None),
                                                      ('fs_free', 23716.22265625, None, None, 0, None),
                                                      ('fs_used_percent', 0.07981958469787793, 80.0, 90.0, 0.0, 100.0),
                                                      ('fs_size', 23735.16796875, None, None, 0, None)]),
            (0, '', [('inodes_used', 4623, 5468582.7, 5772392.85, 0.0, 6076203.0)]),
            (0, '3 filesystems', []),
        ]),
        ('group3', {
            **FILESYSTEM_DEFAULT_PARAMS,
            'patterns': (['*'], []),
            'grouping_behaviour': 'mountpoint',
            "item_appearance": "mountpoint",
        }, [(0, 'Used: 22.24% - 69.6 GiB of 313 GiB', [('fs_used', 71308.953125, 256483.0375,
                                                      288543.4171875, 0, None),
                                                     ('fs_free', 249294.84375, None, None, 0, None),
                                                     ('fs_used_percent', 22.242080043987315, 80.0, 90.0, 0.0, 100.0),
                                                     ('fs_size', 320603.796875, None, None, 0, None)]),
            (0, '', [('inodes_used', 1280583, 37681319.7, 39774726.35, 0.0, 41868133.0)]),
            (0, '16 filesystems', [])]),
        ('group4', {
            **FILESYSTEM_DEFAULT_PARAMS,
            'patterns': (['/opt/omd/sites/*'], ['/opt/omd/sites/site[2,4]/*']),
            'grouping_behaviour': 'mountpoint',
            "item_appearance": "mountpoint",
        }, [(0, 'Used: 0.08% - 39.8 MiB of 46.4 GiB', [('fs_used', 39.75390625, 37976.26875,
                                                       42723.30234375, 0, None),
                                                      ('fs_free', 47430.58203125, None, None, 0, None),
                                                      ('fs_used_percent', 0.083744733347454, 80.0, 90.0, 0.0, 100.0),
                                                      ('fs_size', 47470.3359375, None, None, 0, None)]),
            (0, '', [('inodes_used', 9237, 10937165.4, 11544785.7, 0.0, 12152406.0)]),
            (0, '6 filesystems', [])]),
        ('group5', {
            **FILESYSTEM_DEFAULT_PARAMS,
            'patterns': (['/opt/omd/sites/site1*', ''], ['/opt/omd/sites/site10/*', '']),
            'grouping_behaviour': 'mountpoint',
            "item_appearance": "mountpoint",
        }, [(0, 'Used: 0.08% - 6.31 MiB of 7.73 GiB', [('fs_used', 6.30859375,
                                                     6329.378125, 7120.550390625, 0, None),
                                                    ('fs_free', 7905.4140625, None, None, 0, None),
                                                    ('fs_used_percent', 0.07973729646623064, 80.0, 90.0, 0.0, 100.0),
                                                    ('fs_size', 7911.72265625, None, None, 0, None)]),
            (0, '', [('inodes_used', 1541, 1822860.9000000001, 1924130.95, 0.0, 2025401.0)]),
            (0, '1 filesystems', [])]),
    ],
}
