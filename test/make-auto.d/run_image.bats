@test 'ch-run %(tag)s /bin/true' {
    scope %(scope)s
    %(arch_exclude)s
    prerequisites_ok %(tag)s
    if [[ -e "$ch_tardir/%(tag)s".sqfs ]]; then
        img="$ch_mounts/%(tag)s"
    else
        img="$ch_imgdir/%(tag)s"
    fi
    ch-run "$img" /bin/true
    ch-umount "$img" || true
}
