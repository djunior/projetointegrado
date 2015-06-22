#!/bin/bash

#Loading logger
. /usr/local/bin/gosurf_logger.sh

#Loading environment variables
. /usr/local/etc/gosurf

log "Environment variables:"
log "BEACH_ID=$GOSURF_BEACH_ID"
log "BEACH_NAME=$GOSURF_BEACH_NAME"

#Taking pictures and loading environment variable PICTURE_OUTPUT_DIR
. /usr/local/bin/gosurf_take_pictures.sh

log `/usr/bin/compare_histogram $PICTURE_OUTPUT_DIR/* 2>&1`
