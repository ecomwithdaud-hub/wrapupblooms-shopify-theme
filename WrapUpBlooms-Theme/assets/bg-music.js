/**
 * WrapUpBlooms - Romantic Floral Background Melodies Controller
 * Plays calming royalty-free acoustic guitar & piano music automatically on open.
 * Always ON by default; allows visitors to mute/turn off anytime.
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

    // Default is ALWAYS unmuted unless visitor explicitly clicked OFF in this session
    let isMuted = sessionStorage.getItem(STORAGE_KEY_MUTED) === 'true';

    // Restore playback time from previous page if available
    const savedTime = parseFloat(sessionStorage.getItem(STORAGE_KEY_TIME) || '0');
    if (!isNaN(savedTime) && savedTime > 0) {
      try {
        audio.currentTime = savedTime;
      } catch (e) {}
    }

    function updateBtnUI(muted) {
      if (muted) {
        toggleBtn.classList.add('is-muted');
        toggleBtn.classList.remove('is-waiting');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🔇 Music: OFF';
        toggleBtn.setAttribute('aria-label', 'Turn background music on');
      } else {
        toggleBtn.classList.remove('is-muted', 'is-waiting');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🎵 Music: ON';
        toggleBtn.setAttribute('aria-label', 'Mute background music');
      }
    }

    const unlockEvents = ['click', 'pointerdown', 'touchstart', 'touchend', 'keydown'];

    function removeUnlockListeners() {
      unlockEvents.forEach(function(evt) {
        document.removeEventListener(evt, handleFirstInteraction, true);
        window.removeEventListener(evt, handleFirstInteraction, true);
      });
    }

    function handleFirstInteraction() {
      if (isMuted) return;
      audio.volume = TARGET_VOLUME;
      const p = audio.play();
      if (p !== undefined) {
        p.then(function() {
          // Playback successfully started! Clean up listeners
          removeUnlockListeners();
        }).catch(function() {
          // Not yet unlocked, keep listeners active
        });
      }
    }

    function startPlayback() {
      if (isMuted) return;
      audio.volume = TARGET_VOLUME;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(function() {
          // Immediate autoplay allowed by browser!
        }).catch(function() {
          // Browser requires user interaction: listen for any tap/click anywhere on page
          unlockEvents.forEach(function(evt) {
            document.addEventListener(evt, handleFirstInteraction, { capture: true, passive: true });
            window.addEventListener(evt, handleFirstInteraction, { capture: true, passive: true });
          });
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

    // Toggle button: Allows visitors to turn OFF / turn ON
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (audio.paused || isMuted) {
        isMuted = false;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'false');
        updateBtnUI(false);
        audio.volume = TARGET_VOLUME;
        audio.play().catch(function() {});
      } else {
        isMuted = true;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'true');
        audio.pause();
        updateBtnUI(true);
      }
    });

    // Initial state: ALWAYS ON by default
    updateBtnUI(isMuted);

    if (!isMuted) {
      startPlayback();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMusicPlayer);
  } else {
    initMusicPlayer();
  }
})();
