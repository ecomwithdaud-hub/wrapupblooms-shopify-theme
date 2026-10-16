/**
 * WrapUpBlooms - Romantic Floral Background Melodies Controller
 * Plays calming royalty-free acoustic guitar & piano music across pages.
 * Handles browser autoplay policies, volume fade-in, and cross-page state persistence.
 */
(function() {
  'use strict';

  const STORAGE_KEY_MUTED = 'wrapupblooms_music_muted';
  const STORAGE_KEY_TIME = 'wrapupblooms_music_time';
  const TARGET_VOLUME = 0.28; // Soothing boutique ambient level

  function initMusicPlayer() {
    const audio = document.getElementById('bg-music-player');
    const toggleBtn = document.getElementById('toggle-music');
    if (!audio || !toggleBtn) return;

    // Check saved muted preference (default to unmuted)
    let isMuted = sessionStorage.getItem(STORAGE_KEY_MUTED) === 'true';

    // Restore playback time from previous page if available
    const savedTime = parseFloat(sessionStorage.getItem(STORAGE_KEY_TIME) || '0');
    if (!isNaN(savedTime) && savedTime > 0) {
      audio.currentTime = savedTime;
    }

    function updateBtnUI(muted) {
      if (muted) {
        toggleBtn.classList.add('is-muted');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🔇 Music: OFF';
        toggleBtn.setAttribute('aria-label', 'Turn boutique background music on');
      } else {
        toggleBtn.classList.remove('is-muted');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🎵 Music: ON';
        toggleBtn.setAttribute('aria-label', 'Turn boutique background music off');
      }
    }

    function fadeInAudio() {
      audio.volume = 0;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(function() {
          let vol = 0;
          const interval = setInterval(function() {
            vol += 0.03;
            if (vol >= TARGET_VOLUME) {
              audio.volume = TARGET_VOLUME;
              clearInterval(interval);
            } else {
              audio.volume = vol;
            }
          }, 60);
        }).catch(function(err) {
          // Browser autoplay restriction waiting for first user gesture
        });
      }
    }

    // Continuously save playback timestamp for seamless multi-page browsing
    audio.addEventListener('timeupdate', function() {
      if (!audio.paused && audio.currentTime > 0) {
        sessionStorage.setItem(STORAGE_KEY_TIME, audio.currentTime.toString());
      }
    });

    window.addEventListener('beforeunload', function() {
      if (!audio.paused) {
        sessionStorage.setItem(STORAGE_KEY_TIME, audio.currentTime.toString());
      }
    });

    // Toggle button handler
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (audio.paused || isMuted) {
        isMuted = false;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'false');
        updateBtnUI(false);
        fadeInAudio();
      } else {
        isMuted = true;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'true');
        audio.pause();
        updateBtnUI(true);
      }
    });

    // Set initial UI
    updateBtnUI(isMuted);

    if (!isMuted) {
      // Attempt autoplay
      const startPromise = audio.play();
      if (startPromise !== undefined) {
        startPromise.then(function() {
          audio.volume = TARGET_VOLUME;
        }).catch(function() {
          // Autoplay policy prevented immediate playback; start on first interaction anywhere
          function unlockOnInteraction() {
            if (!isMuted && audio.paused) {
              fadeInAudio();
            }
            ['click', 'touchstart', 'scroll', 'keydown'].forEach(function(evt) {
              window.removeEventListener(evt, unlockOnInteraction);
            });
          }
          ['click', 'touchstart', 'scroll', 'keydown'].forEach(function(evt) {
            window.addEventListener(evt, unlockOnInteraction, { passive: true });
          });
        });
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMusicPlayer);
  } else {
    initMusicPlayer();
  }
})();
