PORTNAME=	zerotier
DISTVERSION=	1.10.2
CATEGORIES=	net

MAINTAINER=	dch@FreeBSD.org
COMMENT=	Network virtualization everywhere
WWW=		https://www.zerotier.com/

# No SaaS or Govt usage: https://github.com/zerotier/ZeroTierOne/blob/master/LICENSE.txt
LICENSE=		BUSINESS MIT PD
LICENSE_COMB=		multi
LICENSE_NAME_BUSINESS=	Business Source License
LICENSE_FILE_BUSINESS=	${WRKSRC}/LICENSE.txt
LICENSE_FILE_MIT=	${WRKSRC}/ext/http-parser/LICENSE-MIT
LICENSE_PERMS_BUSINESS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

BUILD_DEPENDS=	as:devel/binutils

USES=		gmake compiler:c++14-lang
USE_RC_SUBR=	zerotier

USE_GITHUB=	yes
GH_PROJECT=	ZeroTierOne

CFLAGS+=	-flax-vector-conversions

OPTIONS_DEFINE=	DBG
DBG_DESC=	Enable foreground debugging for zerotier-one daemon
DBG_ALL_TARGET=	debug

PLIST_FILES=	bin/zerotier-cli bin/zerotier-idtool sbin/zerotier-one

.include <bsd.port.pre.mk>

.if ${OPSYS} == "FreeBSD"
# log output via syslog
SUB_LIST+=	ZEROTIER_SYSLOG="-s debug -T zerotier"
# after r347241 tun(4) and tap(4) have been merged to tuntap(4)
.if (${OSVERSION} >= 1300028)
SUB_LIST+=	ZEROTIER_IF_TAP="if_tuntap"
.else
SUB_LIST+=	ZEROTIER_IF_TAP="if_tap"
.endif
.else
# we are not on FreeBSD
SUB_LIST+=	ZEROTIER_IF_TAP="if_tap" \
		ZEROTIER_SYSLOG=""
.endif

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/zerotier-one ${STAGEDIR}${PREFIX}/sbin/
.for l in zerotier-cli zerotier-idtool
	${RLN} ${STAGEDIR}${PREFIX}/sbin/zerotier-one ${STAGEDIR}${PREFIX}/bin/${l}
.endfor

.include <bsd.port.post.mk>
