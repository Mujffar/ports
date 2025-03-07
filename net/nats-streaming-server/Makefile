PORTNAME=	nats-streaming-server
PORTVERSION=	0.25.2
DISTVERSIONPREFIX=	v
PORTREVISION=	0
CATEGORIES=	net

MAINTAINER=	olgeni@FreeBSD.org
COMMENT=	Streaming system server for NATS
WWW=		https://nats.io/

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules
USE_GITHUB=	yes
GH_ACCOUNT=	nats-io
GH_TUPLE=	armon:go-metrics:ec5e00d3c878:armon_go_metrics/vendor/github.com/armon/go-metrics \
		etcd-io:bbolt:v1.3.6:etcd_io_bbolt/vendor/go.etcd.io/bbolt \
		fatih:color:v1.7.0:fatih_color/vendor/github.com/fatih/color \
		go-sql-driver:mysql:v1.6.0:go_sql_driver_mysql/vendor/github.com/go-sql-driver/mysql \
		gogo:protobuf:v1.3.2:gogo_protobuf/vendor/github.com/gogo/protobuf \
		golang:crypto:d6f0a8c073c2:golang_crypto/vendor/golang.org/x/crypto \
		golang:sys:090e33056c14:golang_sys/vendor/golang.org/x/sys \
		golang:time:f3bd1da661af:golang_time/vendor/golang.org/x/time \
		hashicorp:go-hclog:v1.1.0:hashicorp_go_hclog/vendor/github.com/hashicorp/go-hclog \
		hashicorp:go-immutable-radix:v1.0.0:hashicorp_go_immutable_radix/vendor/github.com/hashicorp/go-immutable-radix \
		hashicorp:go-msgpack:v1.1.5:hashicorp_go_msgpack/vendor/github.com/hashicorp/go-msgpack \
		hashicorp:golang-lru:v0.5.0:hashicorp_golang_lru/vendor/github.com/hashicorp/golang-lru \
		hashicorp:raft:v1.3.11:hashicorp_raft/vendor/github.com/hashicorp/raft \
		klauspost:compress:v1.15.11:klauspost_compress/vendor/github.com/klauspost/compress \
		lib:pq:v1.10.4:lib_pq/vendor/github.com/lib/pq \
		mattn:go-colorable:v0.1.4:mattn_go_colorable/vendor/github.com/mattn/go-colorable \
		mattn:go-isatty:v0.0.10:mattn_go_isatty/vendor/github.com/mattn/go-isatty \
		minio:highwayhash:v1.0.2:minio_highwayhash/vendor/github.com/minio/highwayhash \
		nats-io:jwt:v2.3.0:nats_io_jwt_v2/vendor/github.com/nats-io/jwt \
		nats-io:nats-server:v2.9.3:nats_io_nats_server_v2/vendor/github.com/nats-io/nats-server/v2 \
		nats-io:nats.go:v1.17.0:nats_io_nats_go/vendor/github.com/nats-io/nats.go \
		nats-io:nkeys:v0.3.0:nats_io_nkeys/vendor/github.com/nats-io/nkeys \
		nats-io:nuid:v1.0.1:nats_io_nuid/vendor/github.com/nats-io/nuid \
		nats-io:stan.go:v0.10.3:nats_io_stan_go/vendor/github.com/nats-io/stan.go \
		prometheus:procfs:v0.8.0:prometheus_procfs/vendor/github.com/prometheus/procfs

USE_RC_SUBR=	nats_streaming.sh
GO_BUILDFLAGS=	-buildvcs=false

OPTIONS_DEFINE=	DOCS

post-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/etc
	${INSTALL_SCRIPT} ${FILESDIR}/nats_streaming.conf ${STAGEDIR}${PREFIX}/etc/nats_streaming.conf.sample
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README.md ${STAGEDIR}${DOCSDIR}

.include <bsd.port.mk>
