PORTNAME=	suitesparse
PORTVERSION=	6.0.1
CATEGORIES=	math

MAINTAINER=	fortran@FreeBSD.org
COMMENT=	Set of packages for sparse matrix calculation
WWW=		https://faculty.cse.tamu.edu/davis/suitesparse.html

RUN_DEPENDS=	suitesparse-amd>0:math/suitesparse-amd			\
		suitesparse-btf>0:math/suitesparse-btf			\
		suitesparse-ccolamd>0:math/suitesparse-ccolamd		\
		suitesparse-cholmod>0:math/suitesparse-cholmod		\
		suitesparse-colamd>0:math/suitesparse-colamd		\
		suitesparse-config>0:math/suitesparse-config		\
		suitesparse-cxsparse>0:math/suitesparse-cxsparse	\
		suitesparse-graphblas>0:math/suitesparse-graphblas	\
		suitesparse-klu>0:math/suitesparse-klu			\
		suitesparse-ldl>0:math/suitesparse-ldl			\
		suitesparse-mongoose>0:math/suitesparse-mongoose	\
		suitesparse-rbio>0:math/suitesparse-rbio		\
		suitesparse-spex>0:math/suitesparse-spex		\
		suitesparse-spqr>0:math/suitesparse-spqr		\
		suitesparse-umfpack>0:math/suitesparse-umfpack
.if !defined(PACKAGE_BUILDING)
RUN_DEPENDS+=	suitesparse-csparse>0:math/suitesparse-csparse
.endif

USES=		metaport

.include <bsd.port.mk>
