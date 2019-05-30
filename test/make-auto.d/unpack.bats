@test 'unpack %(tag)s' {
    scope %(scope)s
    %(arch_exclude)s
    prerequisites_ok %(tag)s
    if [[ -e "$ch_tardir/%(tag)s".sqfs ]]; then
        unsquashfs -d "$ch_imgdir/%(tag)s" "$ch_tardir/%(tag)s".sqfs
        ch-mount "$ch_tardir/%(tag)s".sqfs "$ch_mounts"
    else
        ch-tar2dir "$ch_tardir/%(tag)s" "$ch_imgdir"
    fi
}
