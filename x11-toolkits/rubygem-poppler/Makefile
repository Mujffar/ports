PORTNAME=	poppler
PORTVERSION=	4.0.3
CATEGORIES=	x11-toolkits rubygems
MASTER_SITES=	RG

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Ruby binding of poppler-glib
WWW=		https://ruby-gnome.github.io/

LICENSE=	LGPL21+
LICENSE_FILE=	${WRKSRC}/COPYING.LIB

BUILD_DEPENDS=	rubygem-rake>=0:devel/rubygem-rake
LIB_DEPENDS=	libpoppler-glib.so:graphics/poppler-glib
RUN_DEPENDS=	rubygem-cairo-gobject>=${PORTVERSION}:devel/rubygem-cairo-gobject \
		rubygem-gio2>=${PORTVERSION}:devel/rubygem-gio2

USES=		gem
USE_RUBY=	yes

NO_ARCH=	yes

.include <bsd.port.mk>
