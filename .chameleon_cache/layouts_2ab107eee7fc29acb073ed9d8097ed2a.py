# -*- coding: utf-8 -*-
__filename = '/datos/workspaces/01_github/openttd/inspiration-reference/firs-3.0.9-source/bundle_dir/src/src/templates/layouts.pynml'

__tokens = {658: ('python:industry.industry_layouts', 8, 64), 697: ('tilelayout ${industry_layout.id}_tilelayout {', 9, 4), 710: ('industry_layout.id', 9, 17), 793: ('industry_layout.layout', 10, 50), 830: ('${layout[0]}, ${layout[1]}: ${layout[2]};', 11, 12), 832: ('layout[0]', 11, 14), 846: ('layout[1]', 11, 28), 860: ('layout[2]', 11, 42)}

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
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731879682544
            __attrs_139731879682544 = _static_139731885318736
            __backup_industry_layout_139731882869376 = get('industry_layout', __marker)

            # <Value 'python:industry.industry_layouts' (8:64)> -> __iterator
            __token = 658
            __iterator = _lookup_attr(getitem('industry'), 'industry_layouts')
            (__iterator, ____index_139731879682304, ) = getitem('repeat')('industry_layout', __iterator)
            econtext['industry_layout'] = None
            for __item in __iterator:
                econtext['industry_layout'] = __item

                # <Interpolation value=<Substitution '\n    tilelayout ${industry_layout.id}_tilelayout {\n        ' (8:98)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd0d6790> -> __content_139731891488880
                __token = 697
                __token = 710
                __content_139731891488880 = _lookup_attr(getitem('industry_layout'), 'id')
                __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                __content_139731891488880 = ('%s%s%s' % ('\n    tilelayout ', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), '_tilelayout {\n        ', ))
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

                # <Static value=<ast.Dict object at 0x7f15dd636250> name=None at 7f15dd636820> -> __attrs_139731879685136
                __attrs_139731879685136 = _static_139731885318736
                __backup_layout_139731881302576 = get('layout', __marker)

                # <Value 'industry_layout.layout' (10:50)> -> __iterator
                __token = 793
                __iterator = _lookup_attr(getitem('industry_layout'), 'layout')
                (__iterator, ____index_139731879685088, ) = getitem('repeat')('layout', __iterator)
                econtext['layout'] = None
                for __item in __iterator:
                    econtext['layout'] = __item

                    # <Interpolation value=<Substitution '\n            ${layout[0]}, ${layout[1]}: ${layout[2]};\n        ' (10:74)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f15dd0d6af0> -> __content_139731891488880
                    __token = 830
                    __token = 832
                    __content_139731891488880 = getitem('layout')[0]
                    __content_139731891488880 = __quote(__content_139731891488880, '\x00', '&#0;', None, None)
                    __token = 846
                    __content_139731891488880_844 = getitem('layout')[1]
                    __content_139731891488880_844 = __quote(__content_139731891488880_844, '\x00', '&#0;', None, None)
                    __token = 860
                    __content_139731891488880_858 = getitem('layout')[2]
                    __content_139731891488880_858 = __quote(__content_139731891488880_858, '\x00', '&#0;', None, None)
                    __content_139731891488880 = ('%s%s%s%s%s%s%s' % ('\n            ', (__content_139731891488880 if (__content_139731891488880 is not None) else ''), ', ', (__content_139731891488880_844 if (__content_139731891488880_844 is not None) else ''), ': ', (__content_139731891488880_858 if (__content_139731891488880_858 is not None) else ''), ';\n        ', ))
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
                    ____index_139731879685088 -= 1
                    if (____index_139731879685088 > 0):
                        __append('')
                if (__backup_layout_139731881302576 is __marker):
                    del econtext['layout']
                else:
                    econtext['layout'] = __backup_layout_139731881302576
                __append('\n    }\n')
                ____index_139731879682304 -= 1
                if (____index_139731879682304 > 0):
                    __append('')
            if (__backup_industry_layout_139731882869376 is __marker):
                del econtext['industry_layout']
            else:
                econtext['industry_layout'] = __backup_industry_layout_139731882869376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }