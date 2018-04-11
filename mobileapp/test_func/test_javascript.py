import execjs

javascript_str='''
function i(e, t) {
                var n = (65535 & e) + (65535 & t);
                return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
            }
            function a(e, t) {
                return e << t | e >>> 32 - t
            }
            function s(e, t, n, r, o, s) {
                return i(a(i(i(t, e), i(r, s)), o), n)
            }
            function u(e, t, n, r, o, i, a) {
                return s(t & n | ~t & r, e, t, o, i, a)
            }
            function l(e, t, n, r, o, i, a) {
                return s(t & r | n & ~r, e, t, o, i, a)
            }
            function c(e, t, n, r, o, i, a) {
                return s(t ^ n ^ r, e, t, o, i, a)
            }
            function d(e, t, n, r, o, i, a) {
                return s(n ^ (t | ~r), e, t, o, i, a)
            }
            function f(e, t) {
                e[t >> 5] |= 128 << t % 32,
                e[14 + (t + 64 >>> 9 << 4)] = t;
                var n, r, o, a, s, f = 1732584193, p = -271733879, h = -1732584194, m = 271733878;
                for (n = 0; n < e.length; n += 16)
                    r = f,
                    o = p,
                    a = h,
                    s = m,
                    f = u(f, p, h, m, e[n], 7, -680876936),
                    m = u(m, f, p, h, e[n + 1], 12, -389564586),
                    h = u(h, m, f, p, e[n + 2], 17, 606105819),
                    p = u(p, h, m, f, e[n + 3], 22, -1044525330),
                    f = u(f, p, h, m, e[n + 4], 7, -176418897),
                    m = u(m, f, p, h, e[n + 5], 12, 1200080426),
                    h = u(h, m, f, p, e[n + 6], 17, -1473231341),
                    p = u(p, h, m, f, e[n + 7], 22, -45705983),
                    f = u(f, p, h, m, e[n + 8], 7, 1770035416),
                    m = u(m, f, p, h, e[n + 9], 12, -1958414417),
                    h = u(h, m, f, p, e[n + 10], 17, -42063),
                    p = u(p, h, m, f, e[n + 11], 22, -1990404162),
                    f = u(f, p, h, m, e[n + 12], 7, 1804603682),
                    m = u(m, f, p, h, e[n + 13], 12, -40341101),
                    h = u(h, m, f, p, e[n + 14], 17, -1502002290),
                    p = u(p, h, m, f, e[n + 15], 22, 1236535329),
                    f = l(f, p, h, m, e[n + 1], 5, -165796510),
                    m = l(m, f, p, h, e[n + 6], 9, -1069501632),
                    h = l(h, m, f, p, e[n + 11], 14, 643717713),
                    p = l(p, h, m, f, e[n], 20, -373897302),
                    f = l(f, p, h, m, e[n + 5], 5, -701558691),
                    m = l(m, f, p, h, e[n + 10], 9, 38016083),
                    h = l(h, m, f, p, e[n + 15], 14, -660478335),
                    p = l(p, h, m, f, e[n + 4], 20, -405537848),
                    f = l(f, p, h, m, e[n + 9], 5, 568446438),
                    m = l(m, f, p, h, e[n + 14], 9, -1019803690),
                    h = l(h, m, f, p, e[n + 3], 14, -187363961),
                    p = l(p, h, m, f, e[n + 8], 20, 1163531501),
                    f = l(f, p, h, m, e[n + 13], 5, -1444681467),
                    m = l(m, f, p, h, e[n + 2], 9, -51403784),
                    h = l(h, m, f, p, e[n + 7], 14, 1735328473),
                    p = l(p, h, m, f, e[n + 12], 20, -1926607734),
                    f = c(f, p, h, m, e[n + 5], 4, -378558),
                    m = c(m, f, p, h, e[n + 8], 11, -2022574463),
                    h = c(h, m, f, p, e[n + 11], 16, 1839030562),
                    p = c(p, h, m, f, e[n + 14], 23, -35309556),
                    f = c(f, p, h, m, e[n + 1], 4, -1530992060),
                    m = c(m, f, p, h, e[n + 4], 11, 1272893353),
                    h = c(h, m, f, p, e[n + 7], 16, -155497632),
                    p = c(p, h, m, f, e[n + 10], 23, -1094730640),
                    f = c(f, p, h, m, e[n + 13], 4, 681279174),
                    m = c(m, f, p, h, e[n], 11, -358537222),
                    h = c(h, m, f, p, e[n + 3], 16, -722521979),
                    p = c(p, h, m, f, e[n + 6], 23, 76029189),
                    f = c(f, p, h, m, e[n + 9], 4, -640364487),
                    m = c(m, f, p, h, e[n + 12], 11, -421815835),
                    h = c(h, m, f, p, e[n + 15], 16, 530742520),
                    p = c(p, h, m, f, e[n + 2], 23, -995338651),
                    f = d(f, p, h, m, e[n], 6, -198630844),
                    m = d(m, f, p, h, e[n + 7], 10, 1126891415),
                    h = d(h, m, f, p, e[n + 14], 15, -1416354905),
                    p = d(p, h, m, f, e[n + 5], 21, -57434055),
                    f = d(f, p, h, m, e[n + 12], 6, 1700485571),
                    m = d(m, f, p, h, e[n + 3], 10, -1894986606),
                    h = d(h, m, f, p, e[n + 10], 15, -1051523),
                    p = d(p, h, m, f, e[n + 1], 21, -2054922799),
                    f = d(f, p, h, m, e[n + 8], 6, 1873313359),
                    m = d(m, f, p, h, e[n + 15], 10, -30611744),
                    h = d(h, m, f, p, e[n + 6], 15, -1560198380),
                    p = d(p, h, m, f, e[n + 13], 21, 1309151649),
                    f = d(f, p, h, m, e[n + 4], 6, -145523070),
                    m = d(m, f, p, h, e[n + 11], 10, -1120210379),
                    h = d(h, m, f, p, e[n + 2], 15, 718787259),
                    p = d(p, h, m, f, e[n + 9], 21, -343485551),
                    f = i(f, r),
                    p = i(p, o),
                    h = i(h, a),
                    m = i(m, s);
                return [f, p, h, m]
            }
            function p(e) {
                var t, n = "";
                for (t = 0; t < 32 * e.length; t += 8)
                    n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
                return n
            }
            function h(e) {
                var t, n = [];
                for (n[(e.length >> 2) - 1] = void 0,
                t = 0; t < n.length; t += 1)
                    n[t] = 0;
                for (t = 0; t < 8 * e.length; t += 8)
                    n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
                return n
            }
            function m(e) {
                return p(f(h(e), 8 * e.length))
            }
            function v(e, t) {
                var n, r, o = h(e), i = [], a = [];
                for (i[15] = a[15] = void 0,
                o.length > 16 && (o = f(o, 8 * e.length)),
                n = 0; n < 16; n += 1)
                    i[n] = 909522486 ^ o[n],
                    a[n] = 1549556828 ^ o[n];
                return r = f(i.concat(h(t)), 512 + 8 * t.length),
                p(f(a.concat(r), 640))
            }
            function g(e) {
                var t, n, r = "0123456789abcdef", o = "";
                for (n = 0; n < e.length; n += 1)
                    t = e.charCodeAt(n),
                    o += r.charAt(t >>> 4 & 15) + r.charAt(15 & t);
                return o
            }
            function y(e) {
                return unescape(encodeURIComponent(e))
            }
            function w(e) {
                return m(y(e))
            }
            function _(e) {
                return g(w(e))
            }
            function b(e, t) {
                return v(y(e), y(t))
            }
            function x(e, t) {
                return g(b(e, t))
            }
            function k(e, t, n) {
                return t ? n ? b(t, e) : x(t, e) : n ? w(e) : _(e)
            }
            
            function r() {
            var e = Math.floor((new Date).getTime() / 1e3)
              , t = e.toString(16).toUpperCase()
              , n = k(e).toString().toUpperCase();
            if (8 !== t.length)
                return {
                    as: "479BB4B7254C150",
                    cp: "7E0AC8874BB0985"
                };
            
            
            t1=t.split('');
            
            for (var r = n.slice(0, 5).split(''), i = n.slice(-5), a = "", s = 0; s < 5; s++)
                a += r[s] + t1[s];
            
            i1=i.split('');
            
            for (var u = "", l = 0; l < 5; l++)
                u += t1[l + 3] + i1[l];
                  
                    
            return {
                as: "A1" + a + t.slice(-3),
                cp: t.slice(0, 3) + u + 'E1'
            }
        }

'''

javascript_func=execjs.compile(javascript_str)
print(javascript_func.call('r'))