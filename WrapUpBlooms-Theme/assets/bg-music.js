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

    // Check saved muted preference (default: unmuted)
    let isMuted = sessionStorage.getItem(STORAGE_KEY_MUTED) === 'true';

    // Restore playback time from previous page if available
    const savedTime = parseFloat(sessionStorage.getItem(STORAGE_KEY_TIME) || '0');
    if (!isNaN(savedTime) && savedTime > 0) {
      try {
        audio.currentTime = savedTime;
      } catch (e) {}
    }

    // Set UI state: 'playing' | 'waiting' | 'muted'
    function setUIState(state) {
      toggleBtn.classList.remove('is-muted', 'is-waiting');
      if (state === 'muted') {
        toggleBtn.classList.add('is-muted');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🔇 Music: OFF';
        toggleBtn.setAttribute('aria-label', 'Turn boutique background music on');
      } else if (state === 'playing') {
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🎵 Music: ON';
        toggleBtn.setAttribute('aria-label', 'Turn boutique background music off');
      } else {
        // waiting for user gesture (browser autoplay policy)
        toggleBtn.classList.add('is-waiting');
        toggleBtn.innerHTML = '<span class="music-dot"></span> 🎵 Tap for Music';
        toggleBtn.setAttribute('aria-label', 'Play boutique background music');
      }
    }

    function playAudio() {
      audio.volume = TARGET_VOLUME;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.then(function() {
          setUIState('playing');
        }).catch(function(err) {
          // Still waiting for user gesture
          if (!isMuted) {
            setUIState('waiting');
          }
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

    // Native audio event sync
    audio.addEventListener('play', function() {
      setUIState('playing');
    });

    audio.addEventListener('pause', function() {
      if (isMuted) {
        setUIState('muted');
      } else {
        setUIState('waiting');
      }
    });

    // Toggle button handler
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (audio.paused || isMuted) {
        isMuted = false;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'false');
        playAudio();
      } else {
        isMuted = true;
        sessionStorage.setItem(STORAGE_KEY_MUTED, 'true');
        audio.pause();
        setUIState('muted');
      }
    });

    // Universal first interaction unlock (tap/click anywhere on page)
    const unlockEvents = ['click', 'touchstart', 'touchend', 'pointerdown', 'keydown'];
    function handleFirstInteraction() {
      if (!isMuted && audio.paused) {
        playAudio();
      }
      unlockEvents.forEach(function(evt) {
        document.removeEventListener(evt, handleFirstInteraction, true);
      });
    }

    if (isMuted) {
      setUIState('muted');
    } else {
      // Attempt immediate autoplay
      audio.volume = TARGET_VOLUME;
      const startPromise = audio.play();
      if (startPromise !== undefined) {
        startPromise.then(function() {
          setUIState('playing');
        }).catch(function() {
          // Autoplay blocked by browser policy: set UI to waiting invite
          setUIState('waiting');
          // Unlock on any first user gesture anywhere on the page
          unlockEvents.forEach(function(evt) {
            document.addEventListener(evt, handleFirstInteraction, { capture: true, passive: true });
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
