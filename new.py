import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/Users/ammarkalim/PycharmProjects/mygame',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}
link = "magnet:?xt=urn:btih:0c603cb614f5333716953b8d7b7cbc40f5b3aad2&dn=Dale+Carnegie+-+How+to+Win+Friends+And+Influence+People+%5BWith+Bo&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

print 'downloading metadata...'
while (not handle.has_metadata()):
    time.sleep(1)
print 'got metadata, starting torrent download...'
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
    print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s %d.3' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state],
           s.total_download / 1000000)
    time.sleep(5)
