# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/openttd/resources/firs-3.0.9/src/templates/industry_primary_no_supplies.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1406: ('item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}', 35, 0), 1430: ('industry.id', 35, 24), 1446: ('industry.numeric_id', 35, 40), 1511: ('industry.id', 37, 29), 1645: ('industry.id', 39, 29)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139890621708368 = 'load: properties_industry.pynml'
_static_139890621709472 = "location_checks_industry.macros['render_tree']"
_static_139890621708896 = 'load: availability.pynml'
_static_139890621706640 = 'load: layouts.pynml'
_static_139890621121488 = 'load: properties_tile.pynml'
_static_139890621124464 = "animation_macros.macros['tile_animation']"
_static_139890621123072 = "location_checks_tile.macros['render_tree']"
_static_139890621121008 = 'load: graphics_switches.pynml'
_static_139890623749664 = 'load: spritelayouts.pynml'
_static_139890623748992 = 'load: spritesets.pynml'
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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890623749616
            __attrs_139890623749616 = _static_139890631777632
            __backup_macroname_139890620699328 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2ef9b80> name=None at 7f3ad2ef93a0> -> __value
            __value = _static_139890623748992
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890620699328 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890620699328
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890623746496
            __attrs_139890623746496 = _static_139890631777632
            __backup_macroname_139890623403840 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2ef9e20> name=None at 7f3ad2ef9c40> -> __value
            __value = _static_139890623749664
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890623403840 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890623403840
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621122304
            __attrs_139890621122304 = _static_139890631777632
            __backup_macroname_139890623405760 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2c781f0> name=None at 7f3ad2c78ca0> -> __value
            __value = _static_139890621121008
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890623405760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890623405760
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621120960
            __attrs_139890621120960 = _static_139890631777632
            __backup_location_checks_tile_139890622515184 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139890623403904 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2c78a00> name=None at 7f3ad2c78f10> -> __value
            __value = _static_139890621123072
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890623403904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890623403904
            if (__backup_location_checks_tile_139890622515184 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139890622515184
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621123648
            __attrs_139890621123648 = _static_139890631777632
            __backup_animation_macros_139890621475616 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139890623403200 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2c78f70> name=None at 7f3ad2c787c0> -> __value
            __value = _static_139890621124464
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890623403200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890623403200
            if (__backup_animation_macros_139890621475616 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139890621475616
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621123936
            __attrs_139890621123936 = _static_139890631777632
            __backup_macroname_139890622799936 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2c783d0> name=None at 7f3ad2c787f0> -> __value
            __value = _static_139890621121488
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890622799936 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890622799936
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621706832
            __attrs_139890621706832 = _static_139890631777632
            __backup_macroname_139890631471680 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2d07190> name=None at 7f3ad2d07940> -> __value
            __value = _static_139890621706640
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890631471680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890631471680
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621709232
            __attrs_139890621709232 = _static_139890631777632
            __backup_macroname_139890622429696 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2d07a60> name=None at 7f3ad2d07040> -> __value
            __value = _static_139890621708896
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890622429696 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890622429696
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621708992
            __attrs_139890621708992 = _static_139890631777632
            __backup_location_checks_industry_139890622466368 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139890620699136 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2d07ca0> name=None at 7f3ad2d07160> -> __value
            __value = _static_139890621709472
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890620699136 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890620699136
            if (__backup_location_checks_industry_139890622466368 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139890622466368
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3ad36a1d60> name=None at 7f3ad36a1e20> -> __attrs_139890621706352
            __attrs_139890621706352 = _static_139890631777632
            __backup_macroname_139890622450304 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f3ad2d07850> name=None at 7f3ad2d07970> -> __value
            __value = _static_139890621708368
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139890622450304 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139890622450304
            __append('\n\n\n')

            # <Interpolation value=<Substitution '\nitem(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n' (34:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3ad2d86040> -> __content_139890632639216
            __token = 1406
            __token = 1430
            __content_139890632639216 = _lookup_attr(getitem('industry'), 'id')
            __content_139890632639216 = __quote(__content_139890632639216, '\x00', '&#0;', None, None)
            __token = 1446
            __content_139890632639216_1444 = _lookup_attr(getitem('industry'), 'numeric_id')
            __content_139890632639216_1444 = __quote(__content_139890632639216_1444, '\x00', '&#0;', None, None)
            __token = 1511
            __content_139890632639216_1509 = _lookup_attr(getitem('industry'), 'id')
            __content_139890632639216_1509 = __quote(__content_139890632639216_1509, '\x00', '&#0;', None, None)
            __token = 1645
            __content_139890632639216_1643 = _lookup_attr(getitem('industry'), 'id')
            __content_139890632639216_1643 = __quote(__content_139890632639216_1643, '\x00', '&#0;', None, None)
            __content_139890632639216 = ('%s%s%s%s%s%s%s%s%s' % ('\nitem(FEAT_INDUSTRIES, ', (__content_139890632639216 if (__content_139890632639216 is not None) else ''), ', ', (__content_139890632639216_1444 if (__content_139890632639216_1444 is not None) else ''), ') {\n\tgraphics {\n\t\tconstruction_probability:', (__content_139890632639216_1509 if (__content_139890632639216_1509 is not None) else ''), '_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ', (__content_139890632639216_1643 if (__content_139890632639216_1643 is not None) else ''), '_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n', ))
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
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }