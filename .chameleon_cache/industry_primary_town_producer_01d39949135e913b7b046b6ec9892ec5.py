# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/01_github/openttd/inspiration-reference/firs-3.0.9-source/bundle_dir/src/src/templates/industry_primary_town_producer.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 940: ('load: layouts.pynml', 23, 30), 940: ('load: layouts.pynml', 23, 30), 1149: ('load: location_check_macros_industry.pynml', 29, 46), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1305: ('load: availability.pynml', 32, 30), 1305: ('load: availability.pynml', 32, 30), 1463: ("produce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}", 38, 0), 1473: ('industry.id', 38, 10), 1756: ('industry.id', 48, 34), 1835: ('industry.id', 49, 6), 1863: ('industry.id', 50, 3), 1922: ('load: properties_industry.pynml', 54, 30), 1922: ('load: properties_industry.pynml', 54, 30), 2106: ('economies', 57, 37), 2157: ("industry.get_property('enabled', economy) == True", 58, 39), 2217: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }', 59, 8), 2232: ('economy.numeric_id', 59, 23), 2291: ('industry.id', 60, 36), 2307: ('industry.numeric_id', 60, 52), 2405: ('industry.id', 62, 47), 2474: ('industry.id', 63, 47), 2554: ('industry.id', 64, 47), 2780: ('industry.get_extra_text_fund(economy)', 67, 47)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139731880490992 = 'load: properties_industry.pynml'
_static_139731880490896 = 'load: availability.pynml'
_static_139731880492432 = "location_checks_industry.macros['render_tree']"
_static_139731880492144 = 'load: layouts.pynml'
_static_139731881991952 = 'load: properties_tile.pynml'
_static_139731881990896 = "animation_macros.macros['tile_animation']"
_static_139731880090016 = "location_checks_tile.macros['render_tree']"
_static_139731880089344 = 'load: graphics_switches.pynml'
_static_139731880089152 = 'load: spritelayouts.pynml'
_static_139731880089824 = 'load: spritesets.pynml'
_static_139731885318736 = {}

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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880088768
            __attrs_139731880088768 = _static_139731885318736
            __backup_macroname_139731886014784 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd1398e0> name=None at 7f15dd139df0> -> __value
            __value = _static_139731880089824
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731886014784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731886014784
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880090544
            __attrs_139731880090544 = _static_139731885318736
            __backup_macroname_139731882396928 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139640> name=None at 7f15dd139280> -> __value
            __value = _static_139731880089152
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882396928 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882396928
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880090448
            __attrs_139731880090448 = _static_139731885318736
            __backup_macroname_139731882396224 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139700> name=None at 7f15dd139c10> -> __value
            __value = _static_139731880089344
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882396224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882396224
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880089488
            __attrs_139731880089488 = _static_139731885318736
            __backup_location_checks_tile_139731881451728 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139731882394368 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd1399a0> name=None at 7f15dd139160> -> __value
            __value = _static_139731880090016
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882394368 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882394368
            if (__backup_location_checks_tile_139731881451728 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139731881451728
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731881989264
            __attrs_139731881989264 = _static_139731885318736
            __backup_animation_macros_139731880420208 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139731880785984 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd309af0> name=None at 7f15dd3096d0> -> __value
            __value = _static_139731881990896
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880785984 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880785984
            if (__backup_animation_macros_139731880420208 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139731880420208
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880491472
            __attrs_139731880491472 = _static_139731885318736
            __backup_macroname_139731881523520 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd309f10> name=None at 7f15dd309bb0> -> __value
            __value = _static_139731881991952
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731881523520 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731881523520
            __append('\n\n/* *************************************************\n * Definition of the industry layouts\n * *************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880492624
            __attrs_139731880492624 = _static_139731885318736
            __backup_macroname_139731882768320 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd19bc70> name=None at 7f15dd19b130> -> __value
            __value = _static_139731880492144
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (23:30)> -> __macro
            __token = 940
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 940
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882768320 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882768320
            __append('\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880490656
            __attrs_139731880490656 = _static_139731885318736
            __backup_location_checks_industry_139731882290384 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (29:46)> -> __value
            __token = 1149
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139731881930112 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd19bd90> name=None at 7f15dd19bb50> -> __value
            __value = _static_139731880492432
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (30:30)> -> __macro
            __token = 1223
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1223
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731881930112 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731881930112
            if (__backup_location_checks_industry_139731882290384 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139731882290384
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880491280
            __attrs_139731880491280 = _static_139731885318736
            __backup_macroname_139731882769280 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd19b790> name=None at 7f15dd19ba60> -> __value
            __value = _static_139731880490896
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1305
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1305
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882769280 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882769280
            __append('\n\n')

            # <Interpolation value=<Substitution "\nproduce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}\n\n\n" (37:4)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd19b3d0> -> __content_139731891488880
            __token = 1463
            __token = 1473
            __content_139731891488880 = _lookup_attr(getitem('industry'), 'id')
            __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
            __token = 1756
            __content_139731891488880_1754 = _lookup_attr(getitem('industry'), 'id')
            __content_139731891488880_1754 = __quote(__content_139731891488880_1754, '\x00', '&#0;', None, None)
            __token = 1835
            __content_139731891488880_1833 = _lookup_attr(getitem('industry'), 'id')
            __content_139731891488880_1833 = __quote(__content_139731891488880_1833, '\x00', '&#0;', None, None)
            __token = 1863
            __content_139731891488880_1861 = _lookup_attr(getitem('industry'), 'id')
            __content_139731891488880_1861 = __quote(__content_139731891488880_1861, '\x00', '&#0;', None, None)
            __content_139731891488880 = ('%s%s%s%s%s%s%s%s%s' % ('\nproduce(', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), "_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ", (__content_139731891488880_1754 if (__content_139731891488880_1754 is not None) else ''), '_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ', (__content_139731891488880_1833 if (__content_139731891488880_1833 is not None) else ''), '_production;\n\t', (__content_139731891488880_1861 if (__content_139731891488880_1861 is not None) else ''), '_production;\n}\n\n\n', ))
            if (__content_139731891488880 is None):
                pass
            else:
                if (__content_139731891488880 is None):
                    __content_139731891488880 = None
                else:
                    __tt = type(__content_139731891488880)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139731891488880 = str(__content_139731891488880)
                    else:
                        if (__tt is bytes):
                            __content_139731891488880 = decode(__content_139731891488880)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139731891488880 = __content_139731891488880.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139731891488880)
                                    __content_139731891488880 = (str(__content_139731891488880) if (__content_139731891488880 is __converted) else __converted)
                                else:
                                    __content_139731891488880 = __content_139731891488880()
            if (__content_139731891488880 is not None):
                __append(__content_139731891488880)

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731896296256
            __attrs_139731896296256 = _static_139731885318736
            __backup_macroname_139731882012416 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd19b7f0> name=None at 7f15dd19b430> -> __value
            __value = _static_139731880490992
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (54:30)> -> __macro
            __token = 1922
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1922
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882012416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882012416
            __append('\n\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731896298128
            __attrs_139731896298128 = _static_139731885318736
            __backup_economy_139731882289328 = get('economy', __marker)

            # <Value 'economies' (57:37)> -> __iterator
            __token = 2106
            __iterator = getitem('economies')
            (__iterator, ____index_139731896298464, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731896298608
                __attrs_139731896298608 = _static_139731885318736

                # <Value "industry.get_property('enabled', economy) == True" (58:39)> -> __condition
                __token = 2157
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ' (58:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15de0349a0> -> __content_139731891488880
                    __token = 2217
                    __token = 2232
                    __content_139731891488880 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                    __token = 2291
                    __content_139731891488880_2289 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2289 = __quote(__content_139731891488880_2289, '\x00', '&#0;', None, None)
                    __token = 2307
                    __content_139731891488880_2305 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139731891488880_2305 = __quote(__content_139731891488880_2305, '\x00', '&#0;', None, None)
                    __token = 2405
                    __content_139731891488880_2403 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2403 = __quote(__content_139731891488880_2403, '\x00', '&#0;', None, None)
                    __token = 2474
                    __content_139731891488880_2472 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2472 = __quote(__content_139731891488880_2472, '\x00', '&#0;', None, None)
                    __token = 2554
                    __content_139731891488880_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2552 = __quote(__content_139731891488880_2552, '\x00', '&#0;', None, None)
                    __token = 2780
                    __content_139731891488880_2778 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139731891488880_2778 = __quote(__content_139731891488880_2778, '\x00', '&#0;', None, None)
                    __content_139731891488880 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139731891488880_2289 if (__content_139731891488880_2289 is not None) else ''), ', ', (__content_139731891488880_2305 if (__content_139731891488880_2305 is not None) else ''), ') {\n                graphics {\n                    produce_256_ticks:       ', (__content_139731891488880_2403 if (__content_139731891488880_2403 is not None) else ''), '_produce;\n                    construction_probability:', (__content_139731891488880_2472 if (__content_139731891488880_2472 is not None) else ''), '_check_availability;\n                    location_check:          ', (__content_139731891488880_2552 if (__content_139731891488880_2552 is not None) else ''), '_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ', (__content_139731891488880_2778 if (__content_139731891488880_2778 is not None) else ''), ';\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ', ))
                    if (__content_139731891488880 is None):
                        pass
                    else:
                        if (__content_139731891488880 is None):
                            __content_139731891488880 = None
                        else:
                            __tt = type(__content_139731891488880)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139731891488880 = str(__content_139731891488880)
                            else:
                                if (__tt is bytes):
                                    __content_139731891488880 = decode(__content_139731891488880)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139731891488880 = __content_139731891488880.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139731891488880)
                                            __content_139731891488880 = (str(__content_139731891488880) if (__content_139731891488880 is __converted) else __converted)
                                        else:
                                            __content_139731891488880 = __content_139731891488880()
                    if (__content_139731891488880 is not None):
                        __append(__content_139731891488880)
                __append('\n')
                ____index_139731896298464 -= 1
                if (____index_139731896298464 > 0):
                    __append('')
            if (__backup_economy_139731882289328 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139731882289328
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }