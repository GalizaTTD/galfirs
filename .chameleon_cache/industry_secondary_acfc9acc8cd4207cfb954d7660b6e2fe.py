# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/01_github/openttd/inspiration-reference/firs-3.0.9-source/bundle_dir/src/src/templates/industry_secondary.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: produce_secondary.pynml', 26, 30), 988: ('load: produce_secondary.pynml', 26, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1186: ('load: availability.pynml', 32, 30), 1186: ('load: availability.pynml', 32, 30), 1262: ('load: location_check_macros_industry.pynml', 34, 46), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1602: ('economies', 40, 37), 1653: ("industry.get_property('enabled', economy) == True", 41, 39), 1713: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1728: ('economy.numeric_id', 42, 23), 1787: ('industry.id', 43, 36), 1803: ('industry.numeric_id', 43, 52), 1902: ('industry.id', 45, 48), 1983: ('industry.id', 46, 48), 2053: ('industry.id', 47, 48), 2148: ('industry.id', 48, 48), 2234: ('industry.id', 49, 48), 2311: ('industry.get_extra_text_fund(economy)', 50, 48), 2399: ('industry.id', 51, 48), 2472: ('industry.id', 52, 48)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139731883051952 = 'load: properties_industry.pynml'
_static_139731882869184 = "location_checks_industry.macros['render_tree']"
_static_139731882870864 = 'load: availability.pynml'
_static_139731882870192 = 'load: extra_text_secondary.pynml'
_static_139731882871920 = 'load: closure_secondary.pynml'
_static_139731882872592 = 'load: produce_secondary.pynml'
_static_139731883006608 = 'load: layouts.pynml'
_static_139731883005600 = 'load: properties_tile.pynml'
_static_139731883006704 = "animation_macros.macros['tile_animation']"
_static_139731882858528 = "location_checks_tile.macros['render_tree']"
_static_139731882858288 = 'load: graphics_switches.pynml'
_static_139731882859152 = 'load: spritelayouts.pynml'
_static_139731882859392 = 'load: spritesets.pynml'
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

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882858240
            __attrs_139731882858240 = _static_139731885318736
            __backup_macroname_139731883104640 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3ddb80> name=None at 7f15dd3dd8e0> -> __value
            __value = _static_139731882859392
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731883104640 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731883104640
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882857808
            __attrs_139731882857808 = _static_139731885318736
            __backup_macroname_139731882685760 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3dda90> name=None at 7f15dd3ddf40> -> __value
            __value = _static_139731882859152
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882685760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882685760
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882858816
            __attrs_139731882858816 = _static_139731885318736
            __backup_macroname_139731882800000 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3dd730> name=None at 7f15dd3dd220> -> __value
            __value = _static_139731882858288
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882800000 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882800000
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882860112
            __attrs_139731882860112 = _static_139731885318736
            __backup_location_checks_tile_139731896296736 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139731882950592 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3dd820> name=None at 7f15dd3dd6a0> -> __value
            __value = _static_139731882858528
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882950592 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882950592
            if (__backup_location_checks_tile_139731896296736 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139731896296736
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883004064
            __attrs_139731883004064 = _static_139731885318736
            __backup_animation_macros_139731882935248 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139731882394304 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd401af0> name=None at 7f15dd401b50> -> __value
            __value = _static_139731883006704
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882394304 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882394304
            if (__backup_animation_macros_139731882935248 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139731882935248
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883007280
            __attrs_139731883007280 = _static_139731885318736
            __backup_macroname_139731882395776 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd4016a0> name=None at 7f15dd401220> -> __value
            __value = _static_139731883005600
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882395776 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882395776
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883005408
            __attrs_139731883005408 = _static_139731885318736
            __backup_macroname_139731882397056 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd401a90> name=None at 7f15dd401fd0> -> __value
            __value = _static_139731883006608
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882397056 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882397056
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882871152
            __attrs_139731882871152 = _static_139731885318736
            __backup_macroname_139731882133568 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e0f10> name=None at 7f15dd3e0d90> -> __value
            __value = _static_139731882872592
            econtext['macroname'] = __value

            # <Value 'load: produce_secondary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' produce_secondary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882133568 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882133568
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882871536
            __attrs_139731882871536 = _static_139731885318736
            __backup_macroname_139731882133248 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e0c70> name=None at 7f15dd3e0d00> -> __value
            __value = _static_139731882871920
            econtext['macroname'] = __value

            # <Value 'load: closure_secondary.pynml' (28:30)> -> __macro
            __token = 1053
            __macro = ' closure_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1053
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882133248 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882133248
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882872448
            __attrs_139731882872448 = _static_139731885318736
            __backup_macroname_139731882732480 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e05b0> name=None at 7f15dd3e09a0> -> __value
            __value = _static_139731882870192
            econtext['macroname'] = __value

            # <Value 'load: extra_text_secondary.pynml' (30:30)> -> __macro
            __token = 1118
            __macro = ' extra_text_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1118
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882732480 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882732480
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882871104
            __attrs_139731882871104 = _static_139731885318736
            __backup_macroname_139731882147392 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e0850> name=None at 7f15dd3e0fa0> -> __value
            __value = _static_139731882870864
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1186
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1186
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882147392 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882147392
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731882869952
            __attrs_139731882869952 = _static_139731885318736
            __backup_location_checks_industry_139731896298368 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1262
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139731882146880 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd3e01c0> name=None at 7f15dd3e0df0> -> __value
            __value = _static_139731882869184
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1336
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1336
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882146880 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882146880
            if (__backup_location_checks_industry_139731896298368 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139731896298368
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883051568
            __attrs_139731883051568 = _static_139731885318736
            __backup_macroname_139731882143936 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f15dd40cbb0> name=None at 7f15dd40ce80> -> __value
            __value = _static_139731883051952
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1418
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1418
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139731882143936 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139731882143936
            __append('\n\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883050752
            __attrs_139731883050752 = _static_139731885318736
            __backup_economy_139731895796448 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1602
            __iterator = getitem('economies')
            (__iterator, ____index_139731883052048, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883052864
                __attrs_139731883052864 = _static_139731885318736

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1653
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd40cd60> -> __content_139731891488880
                    __token = 1713
                    __token = 1728
                    __content_139731891488880 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                    __token = 1787
                    __content_139731891488880_1785 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_1785 = __quote(__content_139731891488880_1785, '\x00', '&#0;', None, None)
                    __token = 1803
                    __content_139731891488880_1801 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139731891488880_1801 = __quote(__content_139731891488880_1801, '\x00', '&#0;', None, None)
                    __token = 1902
                    __content_139731891488880_1900 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_1900 = __quote(__content_139731891488880_1900, '\x00', '&#0;', None, None)
                    __token = 1983
                    __content_139731891488880_1981 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_1981 = __quote(__content_139731891488880_1981, '\x00', '&#0;', None, None)
                    __token = 2053
                    __content_139731891488880_2051 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2051 = __quote(__content_139731891488880_2051, '\x00', '&#0;', None, None)
                    __token = 2148
                    __content_139731891488880_2146 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2146 = __quote(__content_139731891488880_2146, '\x00', '&#0;', None, None)
                    __token = 2234
                    __content_139731891488880_2232 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2232 = __quote(__content_139731891488880_2232, '\x00', '&#0;', None, None)
                    __token = 2311
                    __content_139731891488880_2309 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139731891488880_2309 = __quote(__content_139731891488880_2309, '\x00', '&#0;', None, None)
                    __token = 2399
                    __content_139731891488880_2397 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2397 = __quote(__content_139731891488880_2397, '\x00', '&#0;', None, None)
                    __token = 2472
                    __content_139731891488880_2470 = _lookup_attr(getitem('industry'), 'id')
                    __content_139731891488880_2470 = __quote(__content_139731891488880_2470, '\x00', '&#0;', None, None)
                    __content_139731891488880 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139731891488880_1785 if (__content_139731891488880_1785 is not None) else ''), ', ', (__content_139731891488880_1801 if (__content_139731891488880_1801 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_139731891488880_1900 if (__content_139731891488880_1900 is not None) else ''), '_check_availability;\n                    produce_cargo_arrival:    ', (__content_139731891488880_1981 if (__content_139731891488880_1981 is not None) else ''), '_produce;\n                    monthly_prod_change:      ', (__content_139731891488880_2051 if (__content_139731891488880_2051 is not None) else ''), '_check_secondary_production_level;\n                    random_prod_change:       ', (__content_139731891488880_2146 if (__content_139731891488880_2146 is not None) else ''), '_check_secondary_closure;\n                    location_check:           ', (__content_139731891488880_2232 if (__content_139731891488880_2232 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_139731891488880_2309 if (__content_139731891488880_2309 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_139731891488880_2397 if (__content_139731891488880_2397 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_139731891488880_2470 if (__content_139731891488880_2470 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                ____index_139731883052048 -= 1
                if (____index_139731883052048 > 0):
                    __append('')
            if (__backup_economy_139731895796448 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139731895796448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }