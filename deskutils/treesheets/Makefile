PORTNAME=	treesheets
DISTVERSION=	1.0.20221027
CATEGORIES=	deskutils

MAINTAINER=	eduardo@FreeBSD.org
COMMENT=	Free form data organizer
WWW=		https://strlen.com/treesheets/

LICENSE=	ZLIB
LICENSE_FILE=	${WRKSRC}/ZLIB_LICENSE.txt

USES=		cmake compiler:c++17-lang desktop-file-utils gettext gnome

USE_GITHUB=	yes
GH_ACCOUNT=	aardappel
GH_TAGNAME=	3341041135
USE_WX=		3.2

PORTSCOUT=	ignore:1 # upstream uses CI run ids as releases

PORTDATA=	images scripts
PORTDOCS=	docs readme.html
PORTEXAMPLES=	examples

OPTIONS_DEFINE=	DOCS EXAMPLES

post-patch:
	@${REINPLACE_CMD} -e 's|%%EXAMPLESDIR%%|${EXAMPLESDIR}|' ${WRKSRC}/CMakeLists.txt

.include <bsd.port.mk>
