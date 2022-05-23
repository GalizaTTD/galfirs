# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/openttd/resources/firs-3.0.9/src/templates/spritesets.pynml'

__tokens = {634: ('python:industry.spritesets', 8, 40), 824: ('range(len(industry.graphics_change_dates)+1)', 11, 52), 971: ("spriteset.type == ''", 13, 52), 1006: ('spriteset(${spriteset.id}_${date_variation_num}) {', 14, 12), 1018: ('spriteset.id', 14, 24), 1034: ('date_variation_num', 14, 40), 1118: ('range(spriteset.num_sprites_to_autofill)', 15, 61), 1215: ('spriteset.sprites', 16, 54), 1259: ('[${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(date_variation_num)}]', 17, 24), 1262: ('sprite[0]', 17, 27), 1276: ('sprite[1]', 17, 41), 1290: ('sprite[2]', 17, 55), 1304: ('sprite[3]', 17, 69), 1318: ('sprite[4]', 17, 83), 1332: ('sprite[5]', 17, 97), 1361: ('industry.get_graphics_file_path(date_variation_num)', 17, 126), 1508: ('}\n            spriteset(${spriteset.id}_${date_variation_num}_snow) {', 20, 12), 1534: ('spriteset.id', 21, 24), 1550: ('date_variation_num', 21, 40), 1639: ('range(spriteset.num_sprites_to_autofill)', 22, 61), 1736: ('spriteset.sprites', 23, 54), 1784: ("[${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(date_variation_num, terrain='_snow')}]", 24, 28), 1787: ('sprite[0]', 24, 31), 1801: ('sprite[1]', 24, 45), 1815: ('sprite[2]', 24, 59), 1829: ('sprite[3]', 24, 73), 1843: ('sprite[4]', 24, 87), 1857: ('sprite[5]', 24, 101), 1886: ("industry.get_graphics_file_path(date_variation_num, terrain='_snow')", 24, 130), 2237: ("spriteset.type != ''", 31, 31), 2272: ('spriteset(${spriteset.id}_${date_variation_num}, "src/graphics/industries/groundtiles.png") {', 32, 12), 2284: ('spriteset.id', 32, 24), 2300: ('date_variation_num', 32, 40), 2427: ('range(spriteset.num_sprites_to_autofill)', 33, 61), 2490: ('tmpl_ground_tile(${spriteset.get_ground_tile_x_start(spriteset.type)}, 10)', 34, 20), 2509: ('spriteset.get_ground_tile_x_start(spriteset.type)', 34, 39), 2617: ('}\n            spriteset(${spriteset.id}_${date_variation_num}_snow, "src/graphics/industries/groundtiles.png") {', 36, 12), 2643: ('spriteset.id', 37, 24), 2659: ('date_variation_num', 37, 40), 2791: ('range(spriteset.num_sprites_to_autofill)', 38, 61), 2854: ("tmpl_ground_tile(${spriteset.get_ground_tile_x_start('snow')}, 10)", 39, 20), 2873: ("spriteset.get_ground_tile_x_start('snow')", 39, 39), 3066: ("spriteset.type == '' and industry.default_industry_properties.override_default_construction_states==True", 46, 40), 3253: ('range(3)', 48, 42), 3276: ('spriteset(${spriteset.id}_spriteset_default_construction_state_${state_num}) {', 49, 12), 3288: ('spriteset.id', 49, 24), 3341: ('state_num', 49, 77), 3416: ('range(spriteset.num_sprites_to_autofill)', 50, 61), 3513: ('spriteset.sprites', 51, 54), 3557: ('[${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(construction_state_num=state_num)}]', 52, 24), 3560: ('sprite[0]', 52, 27), 3574: ('sprite[1]', 52, 41), 3588: ('sprite[2]', 52, 55), 3602: ('sprite[3]', 52, 69), 3616: ('sprite[4]', 52, 83), 3630: ('sprite[5]', 52, 97), 3659: ('industry.get_graphics_file_path(construction_state_num=state_num)', 52, 126)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139890631777632 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622598016
            __attrs_139890622598016 = _static_139890631777632
            __backup_spriteset_139890622924736 = get('spriteset', __marker)

            # <Value 'python:industry.spritesets' (8:40)> -> __iterator
            __token = 634
            __iterator = _lookup_attr(getitem('industry'), 'spritesets')
            (__iterator, ____index_139890622598544, ) = getitem('repeat')('spriteset', __iterator)
            econtext['spriteset'] = None
            for __item in __iterator:
                econtext['spriteset'] = __item
                __append('\n    \n\n    ')

                # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622598784
                __attrs_139890622598784 = _static_139890631777632
                __backup_date_variation_num_139890622542560 = get('date_variation_num', __marker)

                # <Value 'range(len(industry.graphics_change_dates)+1)' (11:52)> -> __iterator
                __token = 824
                __iterator = get('range', range)((len(_lookup_attr(getitem('industry'), 'graphics_change_dates')) + 1))
                (__iterator, ____index_139890622597632, ) = getitem('repeat')('date_variation_num', __iterator)
                econtext['date_variation_num'] = None
                for __item in __iterator:
                    econtext['date_variation_num'] = __item
                    __append('\n        \n        ')

                    # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622782816
                    __attrs_139890622782816 = _static_139890631777632

                    # <Value "spriteset.type == ''" (13:52)> -> __condition
                    __token = 971
                    __condition = (_lookup_attr(getitem('spriteset'), 'type') == '')
                    if __condition:

                        # <Interpolation value=<Substitution '\n            spriteset(${spriteset.id}_${date_variation_num}) {\n                ' (13:74)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2e0de80> -> __content_139890632639216
                        __token = 1006
                        __token = 1018
                        __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'id')
                        __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                        __token = 1034
                        __content_139890632639216_1032 = getitem('date_variation_num')
                        __content_139890632639216_1032 = __quote(__content_139890632639216_1032, '\x00', '&#0;', None, None)
                        __content_139890632639216 = ('%s%s%s%s%s' % ('\n            spriteset(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), '_', (__content_139890632639216_1032 if (__content_139890632639216_1032 is not None) else ''), ') {\n                ', ))
                        if (__content_139890632639216 is None):
                            pass
                        else:
                            if (__content_139890632639216 is None):
                                __content_139890632639216 = None
                            else:
                                __tt = type(__content_139890632639216)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139890632639216 = str(__content_139890632639216)
                                else:
                                    if (__tt is bytes):
                                        __content_139890632639216 = decode(__content_139890632639216)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139890632639216 = __content_139890632639216.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139890632639216)
                                                __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                            else:
                                                __content_139890632639216 = __content_139890632639216()
                        if (__content_139890632639216 is not None):
                            __append(__content_139890632639216)

                        # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622782432
                        __attrs_139890622782432 = _static_139890631777632
                        __backup_autosprite_num_139890622544768 = get('autosprite_num', __marker)

                        # <Value 'range(spriteset.num_sprites_to_autofill)' (15:61)> -> __iterator
                        __token = 1118
                        __iterator = get('range', range)(_lookup_attr(getitem('spriteset'), 'num_sprites_to_autofill'))
                        (__iterator, ____index_139890622782096, ) = getitem('repeat')('autosprite_num', __iterator)
                        econtext['autosprite_num'] = None
                        for __item in __iterator:
                            econtext['autosprite_num'] = __item
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622780176
                            __attrs_139890622780176 = _static_139890631777632
                            __backup_sprite_139890622544576 = get('sprite', __marker)

                            # <Value 'spriteset.sprites' (16:54)> -> __iterator
                            __token = 1215
                            __iterator = _lookup_attr(getitem('spriteset'), 'sprites')
                            (__iterator, ____index_139890622783152, ) = getitem('repeat')('sprite', __iterator)
                            econtext['sprite'] = None
                            for __item in __iterator:
                                econtext['sprite'] = __item

                                # <Interpolation value=<Substitution '\n                        [${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(date_variation_num)}]\n                    ' (16:73)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2e0dee0> -> __content_139890632639216
                                __token = 1259
                                __token = 1262
                                __content_139890632639216 = getitem('sprite')[0]
                                __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                                __token = 1276
                                __content_139890632639216_1274 = getitem('sprite')[1]
                                __content_139890632639216_1274 = __quote(__content_139890632639216_1274, '\x00', '&#0;', None, None)
                                __token = 1290
                                __content_139890632639216_1288 = getitem('sprite')[2]
                                __content_139890632639216_1288 = __quote(__content_139890632639216_1288, '\x00', '&#0;', None, None)
                                __token = 1304
                                __content_139890632639216_1302 = getitem('sprite')[3]
                                __content_139890632639216_1302 = __quote(__content_139890632639216_1302, '\x00', '&#0;', None, None)
                                __token = 1318
                                __content_139890632639216_1316 = getitem('sprite')[4]
                                __content_139890632639216_1316 = __quote(__content_139890632639216_1316, '\x00', '&#0;', None, None)
                                __token = 1332
                                __content_139890632639216_1330 = getitem('sprite')[5]
                                __content_139890632639216_1330 = __quote(__content_139890632639216_1330, '\x00', '&#0;', None, None)
                                __token = 1361
                                __content_139890632639216_1359 = _lookup_attr(getitem('industry'), 'get_graphics_file_path')(getitem('date_variation_num'))
                                __content_139890632639216_1359 = __quote(__content_139890632639216_1359, '\x00', '&#0;', None, None)
                                __content_139890632639216 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                        [', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', ', (__content_139890632639216_1274 if (__content_139890632639216_1274 is not None) else ''), ', ', (__content_139890632639216_1288 if (__content_139890632639216_1288 is not None) else ''), ', ', (__content_139890632639216_1302 if (__content_139890632639216_1302 is not None) else ''), ', ', (__content_139890632639216_1316 if (__content_139890632639216_1316 is not None) else ''), ', ', (__content_139890632639216_1330 if (__content_139890632639216_1330 is not None) else ''), ', ANIM | NOCROP, ', (__content_139890632639216_1359 if (__content_139890632639216_1359 is not None) else ''), ']\n                    ', ))
                                if (__content_139890632639216 is None):
                                    pass
                                else:
                                    if (__content_139890632639216 is None):
                                        __content_139890632639216 = None
                                    else:
                                        __tt = type(__content_139890632639216)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139890632639216 = str(__content_139890632639216)
                                        else:
                                            if (__tt is bytes):
                                                __content_139890632639216 = decode(__content_139890632639216)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139890632639216 = __content_139890632639216.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139890632639216)
                                                        __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                                    else:
                                                        __content_139890632639216 = __content_139890632639216()
                                if (__content_139890632639216 is not None):
                                    __append(__content_139890632639216)
                                ____index_139890622783152 -= 1
                                if (____index_139890622783152 > 0):
                                    __append('')
                            if (__backup_sprite_139890622544576 is __marker):
                                del econtext['sprite']
                            else:
                                econtext['sprite'] = __backup_sprite_139890622544576
                            __append('\n                ')
                            ____index_139890622782096 -= 1
                            if (____index_139890622782096 > 0):
                                __append('')
                        if (__backup_autosprite_num_139890622544768 is __marker):
                            del econtext['autosprite_num']
                        else:
                            econtext['autosprite_num'] = __backup_autosprite_num_139890622544768

                        # <Interpolation value=<Substitution '\n            }\n            spriteset(${spriteset.id}_${date_variation_num}_snow) {\n                ' (19:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2e0d070> -> __content_139890632639216
                        __token = 1508
                        __token = 1534
                        __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'id')
                        __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                        __token = 1550
                        __content_139890632639216_1548 = getitem('date_variation_num')
                        __content_139890632639216_1548 = __quote(__content_139890632639216_1548, '\x00', '&#0;', None, None)
                        __content_139890632639216 = ('%s%s%s%s%s' % ('\n            }\n            spriteset(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), '_', (__content_139890632639216_1548 if (__content_139890632639216_1548 is not None) else ''), '_snow) {\n                ', ))
                        if (__content_139890632639216 is None):
                            pass
                        else:
                            if (__content_139890632639216 is None):
                                __content_139890632639216 = None
                            else:
                                __tt = type(__content_139890632639216)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139890632639216 = str(__content_139890632639216)
                                else:
                                    if (__tt is bytes):
                                        __content_139890632639216 = decode(__content_139890632639216)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139890632639216 = __content_139890632639216.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139890632639216)
                                                __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                            else:
                                                __content_139890632639216 = __content_139890632639216()
                        if (__content_139890632639216 is not None):
                            __append(__content_139890632639216)

                        # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622779792
                        __attrs_139890622779792 = _static_139890631777632
                        __backup_autosprite_num_139890622545440 = get('autosprite_num', __marker)

                        # <Value 'range(spriteset.num_sprites_to_autofill)' (22:61)> -> __iterator
                        __token = 1639
                        __iterator = get('range', range)(_lookup_attr(getitem('spriteset'), 'num_sprites_to_autofill'))
                        (__iterator, ____index_139890622783008, ) = getitem('repeat')('autosprite_num', __iterator)
                        econtext['autosprite_num'] = None
                        for __item in __iterator:
                            econtext['autosprite_num'] = __item
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622704992
                            __attrs_139890622704992 = _static_139890631777632
                            __backup_sprite_139890622595808 = get('sprite', __marker)

                            # <Value 'spriteset.sprites' (23:54)> -> __iterator
                            __token = 1736
                            __iterator = _lookup_attr(getitem('spriteset'), 'sprites')
                            (__iterator, ____index_139890622704752, ) = getitem('repeat')('sprite', __iterator)
                            econtext['sprite'] = None
                            for __item in __iterator:
                                econtext['sprite'] = __item

                                # <Interpolation value=<Substitution "\n                            [${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(date_variation_num, terrain='_snow')}]\n                    " (23:73)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2dfab50> -> __content_139890632639216
                                __token = 1784
                                __token = 1787
                                __content_139890632639216 = getitem('sprite')[0]
                                __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                                __token = 1801
                                __content_139890632639216_1799 = getitem('sprite')[1]
                                __content_139890632639216_1799 = __quote(__content_139890632639216_1799, '\x00', '&#0;', None, None)
                                __token = 1815
                                __content_139890632639216_1813 = getitem('sprite')[2]
                                __content_139890632639216_1813 = __quote(__content_139890632639216_1813, '\x00', '&#0;', None, None)
                                __token = 1829
                                __content_139890632639216_1827 = getitem('sprite')[3]
                                __content_139890632639216_1827 = __quote(__content_139890632639216_1827, '\x00', '&#0;', None, None)
                                __token = 1843
                                __content_139890632639216_1841 = getitem('sprite')[4]
                                __content_139890632639216_1841 = __quote(__content_139890632639216_1841, '\x00', '&#0;', None, None)
                                __token = 1857
                                __content_139890632639216_1855 = getitem('sprite')[5]
                                __content_139890632639216_1855 = __quote(__content_139890632639216_1855, '\x00', '&#0;', None, None)
                                __token = 1886
                                __content_139890632639216_1884 = _lookup_attr(getitem('industry'), 'get_graphics_file_path')(getitem('date_variation_num'), terrain='_snow')
                                __content_139890632639216_1884 = __quote(__content_139890632639216_1884, '\x00', '&#0;', None, None)
                                __content_139890632639216 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                            [', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', ', (__content_139890632639216_1799 if (__content_139890632639216_1799 is not None) else ''), ', ', (__content_139890632639216_1813 if (__content_139890632639216_1813 is not None) else ''), ', ', (__content_139890632639216_1827 if (__content_139890632639216_1827 is not None) else ''), ', ', (__content_139890632639216_1841 if (__content_139890632639216_1841 is not None) else ''), ', ', (__content_139890632639216_1855 if (__content_139890632639216_1855 is not None) else ''), ', ANIM | NOCROP, ', (__content_139890632639216_1884 if (__content_139890632639216_1884 is not None) else ''), ']\n                    ', ))
                                if (__content_139890632639216 is None):
                                    pass
                                else:
                                    if (__content_139890632639216 is None):
                                        __content_139890632639216 = None
                                    else:
                                        __tt = type(__content_139890632639216)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139890632639216 = str(__content_139890632639216)
                                        else:
                                            if (__tt is bytes):
                                                __content_139890632639216 = decode(__content_139890632639216)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139890632639216 = __content_139890632639216.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139890632639216)
                                                        __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                                    else:
                                                        __content_139890632639216 = __content_139890632639216()
                                if (__content_139890632639216 is not None):
                                    __append(__content_139890632639216)
                                ____index_139890622704752 -= 1
                                if (____index_139890622704752 > 0):
                                    __append('')
                            if (__backup_sprite_139890622595808 is __marker):
                                del econtext['sprite']
                            else:
                                econtext['sprite'] = __backup_sprite_139890622595808
                            __append('\n                ')
                            ____index_139890622783008 -= 1
                            if (____index_139890622783008 > 0):
                                __append('')
                        if (__backup_autosprite_num_139890622545440 is __marker):
                            del econtext['autosprite_num']
                        else:
                            econtext['autosprite_num'] = __backup_autosprite_num_139890622545440
                        __append('\n            }\n        ')
                    __append('\n\n        \n        ')

                    # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622780464
                    __attrs_139890622780464 = _static_139890631777632

                    # <Value "spriteset.type != ''" (31:31)> -> __condition
                    __token = 2237
                    __condition = (_lookup_attr(getitem('spriteset'), 'type') != '')
                    if __condition:

                        # <Interpolation value=<Substitution '\n            spriteset(${spriteset.id}_${date_variation_num}, "src/graphics/industries/groundtiles.png") {\n                ' (31:53)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2dfaaf0> -> __content_139890632639216
                        __token = 2272
                        __token = 2284
                        __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'id')
                        __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                        __token = 2300
                        __content_139890632639216_2298 = getitem('date_variation_num')
                        __content_139890632639216_2298 = __quote(__content_139890632639216_2298, '\x00', '&#0;', None, None)
                        __content_139890632639216 = ('%s%s%s%s%s' % ('\n            spriteset(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), '_', (__content_139890632639216_2298 if (__content_139890632639216_2298 is not None) else ''), ', "src/graphics/industries/groundtiles.png") {\n                ', ))
                        if (__content_139890632639216 is None):
                            pass
                        else:
                            if (__content_139890632639216 is None):
                                __content_139890632639216 = None
                            else:
                                __tt = type(__content_139890632639216)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139890632639216 = str(__content_139890632639216)
                                else:
                                    if (__tt is bytes):
                                        __content_139890632639216 = decode(__content_139890632639216)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139890632639216 = __content_139890632639216.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139890632639216)
                                                __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                            else:
                                                __content_139890632639216 = __content_139890632639216()
                        if (__content_139890632639216 is not None):
                            __append(__content_139890632639216)

                        # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622703936
                        __attrs_139890622703936 = _static_139890631777632
                        __backup_autosprite_num_139890622545200 = get('autosprite_num', __marker)

                        # <Value 'range(spriteset.num_sprites_to_autofill)' (33:61)> -> __iterator
                        __token = 2427
                        __iterator = get('range', range)(_lookup_attr(getitem('spriteset'), 'num_sprites_to_autofill'))
                        (__iterator, ____index_139890622703504, ) = getitem('repeat')('autosprite_num', __iterator)
                        econtext['autosprite_num'] = None
                        for __item in __iterator:
                            econtext['autosprite_num'] = __item

                            # <Interpolation value=<Substitution '\n                    tmpl_ground_tile(${spriteset.get_ground_tile_x_start(spriteset.type)}, 10)\n                ' (33:103)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2dfa4c0> -> __content_139890632639216
                            __token = 2490
                            __token = 2509
                            __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'get_ground_tile_x_start')(_lookup_attr(getitem('spriteset'), 'type'))
                            __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                            __content_139890632639216 = ('%s%s%s' % ('\n                    tmpl_ground_tile(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', 10)\n                ', ))
                            if (__content_139890632639216 is None):
                                pass
                            else:
                                if (__content_139890632639216 is None):
                                    __content_139890632639216 = None
                                else:
                                    __tt = type(__content_139890632639216)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139890632639216 = str(__content_139890632639216)
                                    else:
                                        if (__tt is bytes):
                                            __content_139890632639216 = decode(__content_139890632639216)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139890632639216 = __content_139890632639216.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139890632639216)
                                                    __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                                else:
                                                    __content_139890632639216 = __content_139890632639216()
                            if (__content_139890632639216 is not None):
                                __append(__content_139890632639216)
                            ____index_139890622703504 -= 1
                            if (____index_139890622703504 > 0):
                                __append('')
                        if (__backup_autosprite_num_139890622545200 is __marker):
                            del econtext['autosprite_num']
                        else:
                            econtext['autosprite_num'] = __backup_autosprite_num_139890622545200

                        # <Interpolation value=<Substitution '\n            }\n            spriteset(${spriteset.id}_${date_variation_num}_snow, "src/graphics/industries/groundtiles.png") {\n                ' (35:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2dfaa90> -> __content_139890632639216
                        __token = 2617
                        __token = 2643
                        __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'id')
                        __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                        __token = 2659
                        __content_139890632639216_2657 = getitem('date_variation_num')
                        __content_139890632639216_2657 = __quote(__content_139890632639216_2657, '\x00', '&#0;', None, None)
                        __content_139890632639216 = ('%s%s%s%s%s' % ('\n            }\n            spriteset(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), '_', (__content_139890632639216_2657 if (__content_139890632639216_2657 is not None) else ''), '_snow, "src/graphics/industries/groundtiles.png") {\n                ', ))
                        if (__content_139890632639216 is None):
                            pass
                        else:
                            if (__content_139890632639216 is None):
                                __content_139890632639216 = None
                            else:
                                __tt = type(__content_139890632639216)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139890632639216 = str(__content_139890632639216)
                                else:
                                    if (__tt is bytes):
                                        __content_139890632639216 = decode(__content_139890632639216)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139890632639216 = __content_139890632639216.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139890632639216)
                                                __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                            else:
                                                __content_139890632639216 = __content_139890632639216()
                        if (__content_139890632639216 is not None):
                            __append(__content_139890632639216)

                        # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622703168
                        __attrs_139890622703168 = _static_139890631777632
                        __backup_autosprite_num_139890622595184 = get('autosprite_num', __marker)

                        # <Value 'range(spriteset.num_sprites_to_autofill)' (38:61)> -> __iterator
                        __token = 2791
                        __iterator = get('range', range)(_lookup_attr(getitem('spriteset'), 'num_sprites_to_autofill'))
                        (__iterator, ____index_139890622702400, ) = getitem('repeat')('autosprite_num', __iterator)
                        econtext['autosprite_num'] = None
                        for __item in __iterator:
                            econtext['autosprite_num'] = __item

                            # <Interpolation value=<Substitution "\n                    tmpl_ground_tile(${spriteset.get_ground_tile_x_start('snow')}, 10)\n                " (38:103)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2dfa4f0> -> __content_139890632639216
                            __token = 2854
                            __token = 2873
                            __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'get_ground_tile_x_start')('snow')
                            __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                            __content_139890632639216 = ('%s%s%s' % ('\n                    tmpl_ground_tile(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', 10)\n                ', ))
                            if (__content_139890632639216 is None):
                                pass
                            else:
                                if (__content_139890632639216 is None):
                                    __content_139890632639216 = None
                                else:
                                    __tt = type(__content_139890632639216)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139890632639216 = str(__content_139890632639216)
                                    else:
                                        if (__tt is bytes):
                                            __content_139890632639216 = decode(__content_139890632639216)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139890632639216 = __content_139890632639216.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139890632639216)
                                                    __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                                else:
                                                    __content_139890632639216 = __content_139890632639216()
                            if (__content_139890632639216 is not None):
                                __append(__content_139890632639216)
                            ____index_139890622702400 -= 1
                            if (____index_139890622702400 > 0):
                                __append('')
                        if (__backup_autosprite_num_139890622595184 is __marker):
                            del econtext['autosprite_num']
                        else:
                            econtext['autosprite_num'] = __backup_autosprite_num_139890622595184
                        __append('\n            }\n        ')
                    __append('\n    ')
                    ____index_139890622597632 -= 1
                    if (____index_139890622597632 > 0):
                        __append('')
                if (__backup_date_variation_num_139890622542560 is __marker):
                    del econtext['date_variation_num']
                else:
                    econtext['date_variation_num'] = __backup_date_variation_num_139890622542560
                __append('\n\n\n    ')

                # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622782192
                __attrs_139890622782192 = _static_139890631777632

                # <Value "spriteset.type == '' and industry.default_industry_properties.override_default_construction_states==True" (46:40)> -> __condition
                __token = 3066
                __condition = ((_lookup_attr(getitem('spriteset'), 'type') == '') and (_lookup_attr(_lookup_attr(getitem('industry'), 'default_industry_properties'), 'override_default_construction_states') == True))
                if __condition:
                    __append('\n        \n        ')

                    # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622923872
                    __attrs_139890622923872 = _static_139890631777632
                    __backup_state_num_139890622543088 = get('state_num', __marker)

                    # <Value 'range(3)' (48:42)> -> __iterator
                    __token = 3253
                    __iterator = get('range', range)(3)
                    (__iterator, ____index_139890622924496, ) = getitem('repeat')('state_num', __iterator)
                    econtext['state_num'] = None
                    for __item in __iterator:
                        econtext['state_num'] = __item

                        # <Interpolation value=<Substitution '\n            spriteset(${spriteset.id}_spriteset_default_construction_state_${state_num}) {\n                ' (48:52)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2e30fd0> -> __content_139890632639216
                        __token = 3276
                        __token = 3288
                        __content_139890632639216 = _lookup_attr(getitem('spriteset'), 'id')
                        __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                        __token = 3341
                        __content_139890632639216_3339 = getitem('state_num')
                        __content_139890632639216_3339 = __quote(__content_139890632639216_3339, '\x00', '&#0;', None, None)
                        __content_139890632639216 = ('%s%s%s%s%s' % ('\n            spriteset(', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), '_spriteset_default_construction_state_', (__content_139890632639216_3339 if (__content_139890632639216_3339 is not None) else ''), ') {\n                ', ))
                        if (__content_139890632639216 is None):
                            pass
                        else:
                            if (__content_139890632639216 is None):
                                __content_139890632639216 = None
                            else:
                                __tt = type(__content_139890632639216)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139890632639216 = str(__content_139890632639216)
                                else:
                                    if (__tt is bytes):
                                        __content_139890632639216 = decode(__content_139890632639216)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139890632639216 = __content_139890632639216.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139890632639216)
                                                __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                            else:
                                                __content_139890632639216 = __content_139890632639216()
                        if (__content_139890632639216 is not None):
                            __append(__content_139890632639216)

                        # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622926416
                        __attrs_139890622926416 = _static_139890631777632
                        __backup_autosprite_num_139890622596384 = get('autosprite_num', __marker)

                        # <Value 'range(spriteset.num_sprites_to_autofill)' (50:61)> -> __iterator
                        __token = 3416
                        __iterator = get('range', range)(_lookup_attr(getitem('spriteset'), 'num_sprites_to_autofill'))
                        (__iterator, ____index_139890622924640, ) = getitem('repeat')('autosprite_num', __iterator)
                        econtext['autosprite_num'] = None
                        for __item in __iterator:
                            econtext['autosprite_num'] = __item
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890622925024
                            __attrs_139890622925024 = _static_139890631777632
                            __backup_sprite_139890622595856 = get('sprite', __marker)

                            # <Value 'spriteset.sprites' (51:54)> -> __iterator
                            __token = 3513
                            __iterator = _lookup_attr(getitem('spriteset'), 'sprites')
                            (__iterator, ____index_139890622925312, ) = getitem('repeat')('sprite', __iterator)
                            econtext['sprite'] = None
                            for __item in __iterator:
                                econtext['sprite'] = __item

                                # <Interpolation value=<Substitution '\n                        [${sprite[0]}, ${sprite[1]}, ${sprite[2]}, ${sprite[3]}, ${sprite[4]}, ${sprite[5]}, ANIM | NOCROP, ${industry.get_graphics_file_path(construction_state_num=state_num)}]\n                    ' (51:73)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2e30640> -> __content_139890632639216
                                __token = 3557
                                __token = 3560
                                __content_139890632639216 = getitem('sprite')[0]
                                __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
                                __token = 3574
                                __content_139890632639216_3572 = getitem('sprite')[1]
                                __content_139890632639216_3572 = __quote(__content_139890632639216_3572, '\x00', '&#0;', None, None)
                                __token = 3588
                                __content_139890632639216_3586 = getitem('sprite')[2]
                                __content_139890632639216_3586 = __quote(__content_139890632639216_3586, '\x00', '&#0;', None, None)
                                __token = 3602
                                __content_139890632639216_3600 = getitem('sprite')[3]
                                __content_139890632639216_3600 = __quote(__content_139890632639216_3600, '\x00', '&#0;', None, None)
                                __token = 3616
                                __content_139890632639216_3614 = getitem('sprite')[4]
                                __content_139890632639216_3614 = __quote(__content_139890632639216_3614, '\x00', '&#0;', None, None)
                                __token = 3630
                                __content_139890632639216_3628 = getitem('sprite')[5]
                                __content_139890632639216_3628 = __quote(__content_139890632639216_3628, '\x00', '&#0;', None, None)
                                __token = 3659
                                __content_139890632639216_3657 = _lookup_attr(getitem('industry'), 'get_graphics_file_path')(construction_state_num=getitem('state_num'))
                                __content_139890632639216_3657 = __quote(__content_139890632639216_3657, '\x00', '&#0;', None, None)
                                __content_139890632639216 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                        [', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', ', (__content_139890632639216_3572 if (__content_139890632639216_3572 is not None) else ''), ', ', (__content_139890632639216_3586 if (__content_139890632639216_3586 is not None) else ''), ', ', (__content_139890632639216_3600 if (__content_139890632639216_3600 is not None) else ''), ', ', (__content_139890632639216_3614 if (__content_139890632639216_3614 is not None) else ''), ', ', (__content_139890632639216_3628 if (__content_139890632639216_3628 is not None) else ''), ', ANIM | NOCROP, ', (__content_139890632639216_3657 if (__content_139890632639216_3657 is not None) else ''), ']\n                    ', ))
                                if (__content_139890632639216 is None):
                                    pass
                                else:
                                    if (__content_139890632639216 is None):
                                        __content_139890632639216 = None
                                    else:
                                        __tt = type(__content_139890632639216)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139890632639216 = str(__content_139890632639216)
                                        else:
                                            if (__tt is bytes):
                                                __content_139890632639216 = decode(__content_139890632639216)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139890632639216 = __content_139890632639216.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139890632639216)
                                                        __content_139890632639216 = (str(__content_139890632639216) if (__content_139890632639216 is __converted) else __converted)
                                                    else:
                                                        __content_139890632639216 = __content_139890632639216()
                                if (__content_139890632639216 is not None):
                                    __append(__content_139890632639216)
                                ____index_139890622925312 -= 1
                                if (____index_139890622925312 > 0):
                                    __append('')
                            if (__backup_sprite_139890622595856 is __marker):
                                del econtext['sprite']
                            else:
                                econtext['sprite'] = __backup_sprite_139890622595856
                            __append('\n                ')
                            ____index_139890622924640 -= 1
                            if (____index_139890622924640 > 0):
                                __append('')
                        if (__backup_autosprite_num_139890622596384 is __marker):
                            del econtext['autosprite_num']
                        else:
                            econtext['autosprite_num'] = __backup_autosprite_num_139890622596384
                        __append('\n            }\n        ')
                        ____index_139890622924496 -= 1
                        if (____index_139890622924496 > 0):
                            __append('')
                    if (__backup_state_num_139890622543088 is __marker):
                        del econtext['state_num']
                    else:
                        econtext['state_num'] = __backup_state_num_139890622543088
                    __append('\n    ')
                __append('\n')
                ____index_139890622598544 -= 1
                if (____index_139890622598544 > 0):
                    __append('')
            if (__backup_spriteset_139890622924736 is __marker):
                del econtext['spriteset']
            else:
                econtext['spriteset'] = __backup_spriteset_139890622924736
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }