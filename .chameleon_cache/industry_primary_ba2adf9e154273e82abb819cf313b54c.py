# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/01_github/openttd/inspiration-reference/firs-3.0.9-source/bundle_dir/src/src/templates/industry_primary.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1197: ('load: availability.pynml', 32, 30), 1197: ('load: availability.pynml', 32, 30), 1273: ('load: location_check_macros_industry.pynml', 34, 46), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1613: ('economies', 40, 37), 1664: ("industry.get_property('enabled', economy) == True", 41, 39), 1724: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1739: ('economy.numeric_id', 42, 23), 1798: ('industry.id', 43, 36), 1814: ('industry.numeric_id', 43, 52), 1913: ('industry.id', 45, 48), 2079: ('industry.id', 47, 48), 2149: ('industry.id', 48, 48), 2229: ('industry.id', 49, 48), 2389: ('industry.id', 51, 48), 2466: ('industry.get_extra_text_fund(economy)', 52, 48), 2554: ('industry.id', 53, 48), 2627: ('industry.id', 54, 48)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139731879539232 = 'load: properties_industry.pynml'
_static_139731882887920 = "location_checks_industry.macros['render_tree']"
_static_139731882885568 = 'load: availability.pynml'
_static_139731882886912 = 'load: check_primary_supplies_delivered.pynml'
_static_139731882887296 = 'load: produce_primary.pynml'
_static_139731880090880 = 'load: extra_text_primary.pynml'
_static_139731880090688 = 'load: layouts.pynml'
_static_139731880089728 = 'load: properties_tile.pynml'
_static_139731880090304 = "animation_macros.macros['tile_animation']"
_static_139731880089776 = "location_checks_tile.macros['render_tree']"
_static_139731881990368 = 'load: graphics_switches.pynml'
_static_139731881988928 = 'load: spritelayouts.pynml'
_static_139731881991712 = 'load: spritesets.pynml'
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

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731881989984
            __attrs_139731881989984 = _static_139731885318736
            __backup_macroname_139731880099520 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd309e20> name=None at 7f15dd309b50> -> __value
            __value = _static_139731881991712
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880099520 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880099520
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731881992096
            __attrs_139731881992096 = _static_139731885318736
            __backup_macroname_139731880098880 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd309340> name=None at 7f15dd309370> -> __value
            __value = _static_139731881988928
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880098880 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880098880
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731881991856
            __attrs_139731881991856 = _static_139731885318736
            __backup_macroname_139731887700288 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3098e0> name=None at 7f15dd309d90> -> __value
            __value = _static_139731881990368
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731887700288 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731887700288
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880091168
            __attrs_139731880091168 = _static_139731885318736
            __backup_location_checks_tile_139731881300128 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139731885576448 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd1398b0> name=None at 7f15dd139910> -> __value
            __value = _static_139731880089776
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731885576448 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731885576448
            if (__backup_location_checks_tile_139731881300128 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139731881300128
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880090016
            __attrs_139731880090016 = _static_139731885318736
            __backup_animation_macros_139731881646832 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139731883121152 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139ac0> name=None at 7f15dd1398e0> -> __value
            __value = _static_139731880090304
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731883121152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731883121152
            if (__backup_animation_macros_139731881646832 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139731881646832
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880090544
            __attrs_139731880090544 = _static_139731885318736
            __backup_macroname_139731883120192 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139880> name=None at 7f15dd139670> -> __value
            __value = _static_139731880089728
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731883120192 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731883120192
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731880090640
            __attrs_139731880090640 = _static_139731885318736
            __backup_macroname_139731882907712 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139c40> name=None at 7f15dd139100> -> __value
            __value = _static_139731880090688
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882907712 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882907712
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882888112
            __attrs_139731882888112 = _static_139731885318736
            __backup_macroname_139731881535040 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd139d00> name=None at 7f15dd139070> -> __value
            __value = _static_139731880090880
            econtext['macroname'] = __value

            # <Value 'load: extra_text_primary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' extra_text_primary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731881535040 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731881535040
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882886672
            __attrs_139731882886672 = _static_139731885318736
            __backup_macroname_139731880772224 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e4880> name=None at 7f15dd3e4b20> -> __value
            __value = _static_139731882887296
            econtext['macroname'] = __value

            # <Value 'load: produce_primary.pynml' (28:30)> -> __macro
            __token = 1054
            __macro = ' produce_primary.pynml'
            __macro = __loader(__macro)
            __token = 1054
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880772224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880772224
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882889024
            __attrs_139731882889024 = _static_139731885318736
            __backup_macroname_139731880773376 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e4700> name=None at 7f15dd3e47c0> -> __value
            __value = _static_139731882886912
            econtext['macroname'] = __value

            # <Value 'load: check_primary_supplies_delivered.pynml' (30:30)> -> __macro
            __token = 1117
            __macro = ' check_primary_supplies_delivered.pynml'
            __macro = __loader(__macro)
            __token = 1117
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880773376 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880773376
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882888544
            __attrs_139731882888544 = _static_139731885318736
            __backup_macroname_139731880774784 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e41c0> name=None at 7f15dd3e48e0> -> __value
            __value = _static_139731882885568
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1197
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880774784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880774784
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882888208
            __attrs_139731882888208 = _static_139731885318736
            __backup_location_checks_industry_139731881300800 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1273
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139731880204544 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e4af0> name=None at 7f15dd3e4910> -> __value
            __value = _static_139731882887920
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1347
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880204544 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880204544
            if (__backup_location_checks_industry_139731881300800 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139731881300800
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731879541440
            __attrs_139731879541440 = _static_139731885318736
            __backup_macroname_139731880206016 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd0b3220> name=None at 7f15dd0b33d0> -> __value
            __value = _static_139731879539232
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1429
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1429
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731880206016 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731880206016
            __append('\n\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731879538752
            __attrs_139731879538752 = _static_139731885318736
            __backup_economy_139731880492240 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1613
            __iterator = getitem('economies')
            (__iterator, ____index_139731879539184, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731879541152
                __attrs_139731879541152 = _static_139731885318736

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1664
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd0b3a30> -> __content_139731891488880
                    __token = 1724
                    __token = 1739
                    __content_139731891488880 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                    __token = 1798
                    __content_139731891488880_1796 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_1796 = __quote(__content_139731891488880_1796, '\x00', '&#0;', None, None)
                    __token = 1814
                    __content_139731891488880_1812 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139731891488880_1812 = __quote(__content_139731891488880_1812, '\x00', '&#0;', None, None)
                    __token = 1913
                    __content_139731891488880_1911 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_1911 = __quote(__content_139731891488880_1911, '\x00', '&#0;', None, None)
                    __token = 2079
                    __content_139731891488880_2077 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2077 = __quote(__content_139731891488880_2077, '\x00', '&#0;', None, None)
                    __token = 2149
                    __content_139731891488880_2147 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2147 = __quote(__content_139731891488880_2147, '\x00', '&#0;', None, None)
                    __token = 2229
                    __content_139731891488880_2227 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2227 = __quote(__content_139731891488880_2227, '\x00', '&#0;', None, None)
                    __token = 2389
                    __content_139731891488880_2387 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2387 = __quote(__content_139731891488880_2387, '\x00', '&#0;', None, None)
                    __token = 2466
                    __content_139731891488880_2464 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139731891488880_2464 = __quote(__content_139731891488880_2464, '\x00', '&#0;', None, None)
                    __token = 2554
                    __content_139731891488880_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2552 = __quote(__content_139731891488880_2552, '\x00', '&#0;', None, None)
                    __token = 2627
                    __content_139731891488880_2625 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2625 = __quote(__content_139731891488880_2625, '\x00', '&#0;', None, None)
                    __content_139731891488880 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139731891488880_1796 if (__content_139731891488880_1796 is not None) else ''), ', ', (__content_139731891488880_1812 if (__content_139731891488880_1812 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_139731891488880_1911 if (__content_139731891488880_1911 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ', (__content_139731891488880_2077 if (__content_139731891488880_2077 is not None) else ''), '_produce;\n                    produce_256_ticks:        ', (__content_139731891488880_2147 if (__content_139731891488880_2147 is not None) else ''), '_produce_256_ticks;\n                    monthly_prod_change:      ', (__content_139731891488880_2227 if (__content_139731891488880_2227 is not None) else ''), '_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ', (__content_139731891488880_2387 if (__content_139731891488880_2387 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_139731891488880_2464 if (__content_139731891488880_2464 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_139731891488880_2552 if (__content_139731891488880_2552 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_139731891488880_2625 if (__content_139731891488880_2625 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                ____index_139731879539184 -= 1
                if (____index_139731879539184 > 0):
                    __append('')
            if (__backup_economy_139731880492240 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139731880492240
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }