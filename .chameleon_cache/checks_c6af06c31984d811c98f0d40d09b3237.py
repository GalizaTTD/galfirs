# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/01_github/openttd/inspiration-reference/firs-3.0.9-source/bundle_dir/src/src/templates/checks.pynml'

__tokens = {503: ('incompatible_grfs', 14, 48), 527: ('if (grf_future_status("${incompatible_grf.grfid}")) {\n        error(FATAL, string(STR_ERR_INCOMPATIBLE_SET, "${incompatible_grf.grfname}"));\n    }', 15, 4), 552: ('incompatible_grf.grfid', 15, 29), 638: ('incompatible_grf.grfname', 16, 57)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

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
            __append('\n\n\n\n\nif (ttd_platform != PLATFORM_OPENTTD || openttd_version < version_openttd(1, 7, 0, 27769)) {\n\terror(FATAL, REQUIRES_OPENTTD, string(STR_ERR_OPENTTD_VERSION));\n\texit;\n}\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731883005600
            __attrs_139731883005600 = _static_139731885318736
            __backup_incompatible_grf_139731896298416 = get('incompatible_grf', __marker)

            # <Value 'incompatible_grfs' (14:48)> -> __iterator
            __token = 503
            __iterator = getitem('incompatible_grfs')
            (__iterator, ____index_139731883005840, ) = getitem('repeat')('incompatible_grf', __iterator)
            econtext['incompatible_grf'] = None
            for __item in __iterator:
                econtext['incompatible_grf'] = __item

                # <Interpolation value=<Substitution '\n    if (grf_future_status("${incompatible_grf.grfid}")) {\n        error(FATAL, string(STR_ERR_INCOMPATIBLE_SET, "${incompatible_grf.grfname}"));\n    }\n' (14:67)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd401940> -> __content_139731891488880
                __token = 527
                __token = 552
                __content_139731891488880 = _lookup_attr(getitem('incompatible_grf'), 'grfid')
                __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                __token = 638
                __content_139731891488880_636 = _lookup_attr(getitem('incompatible_grf'), 'grfname')
                __content_139731891488880_636 = __quote(__content_139731891488880_636, '\x00', '&#0;', None, None)
                __content_139731891488880 = ('%s%s%s%s%s' % ('\n    if (grf_future_status("', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), '")) {\n        error(FATAL, string(STR_ERR_INCOMPATIBLE_SET, "', (__content_139731891488880_636 if (__content_139731891488880_636 is not None) else ''), '"));\n    }\n', ))
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
                ____index_139731883005840 -= 1
                if (____index_139731883005840 > 0):
                    __append('')
            if (__backup_incompatible_grf_139731896298416 is __marker):
                del econtext['incompatible_grf']
            else:
                econtext['incompatible_grf'] = __backup_incompatible_grf_139731896298416
            __append('\n\n\n\n/* this one might not survive as artic-only\nif (climate == CLIMATE_ARCTIC) {\n\tINCOMPATIBLE_GRF("mb\\07\\00", "Alpine Climate");\n}\n*/\n\nif (grf_future_status("MG\\08\\00", "\\FF\\FF\\FF\\00")) {\n\terror(FATAL, string(STR_ERR_INCOMPATIBLE_SET, "Lumber Mill"));\n}\n\nif (grf_future_status("CACa")) {\n\tif (param["CACa", 1] != 0) {\n\t\terror(FATAL, string(STR_ERR_INCOMPATIBLE_PARAM_CITYSET));\n\t}\n}\nif (grf_future_status("CASa")) {\n\tif (param["CASa", 1] != 0) {\n\t\terror(FATAL, string(STR_ERR_INCOMPATIBLE_PARAM_CANSET));\n\t}\n}\nif (grf_future_status("VC\\00\\01")) {\n\tif (param["VC\\00\\01", 254] <= 17) {\n\t\terror(FATAL, string(STR_ERR_INCOMPATIBLE_SET_TTRS_VERSION));\n\t}\n}\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }