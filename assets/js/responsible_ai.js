let cards = document.getElementsByClassName('card');
// console.log(cards);

let fairness =
    '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/4bqrlZ-CyNs?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

let transparency =
    '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/q5CbK0Hs1pg?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

let reliability =
    '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/i3akj3GHmdw?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

let privacy =
    '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/AZZdMgOe60k?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

let inclusiveness =
    '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/aVgbsRn9zK8?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

let accountability = '<iframe width="100%" height="360" src="https://www.youtube-nocookie.com/embed/5BQ2RE9kqvA?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';


function changeVideo(element, title) {
    // remove white card from all cards
    Array.from(cards).forEach(card => {
        card.classList.remove("selected-card")
    });

    // add white card to active card
    element.classList.add("selected-card");

    // get video div
    let video = document.getElementById("principles-video");

//   change video given the title
    switch (title) {
        case "fairness":
            video.innerHTML = fairness;
            break;
        case "transparency":
            video.innerHTML = transparency;
            break;
        case "privacy":
            video.innerHTML = privacy;
            break;
        case "inclusiveness":
            video.innerHTML = inclusiveness;
            break;
        case "reliability":
            video.innerHTML = reliability;
            break;
        default:
            video.innerHTML = accountability;
            break;
    }
}

function changeYoutubeIconToRed() {
    var youtubeIcon = document.getElementById('youtubeIcon');
    youtubeIcon.src = "../assets/imgs/youtube_red.png"
}

function changeYoutubeIconToBlack() {
    var youtubeIcon = document.getElementById('youtubeIcon');
    youtubeIcon.src = "../assets/imgs/youtube_black.png"
}

function playVideo(element, id) {
    element.style.display = 'none';
    document.getElementById(id).classList.add('showVideo');
    let src = document.getElementById(id).src
    document.getElementById(id).src = src.replace('autoplay=0', 'autoplay=1');

    // this function ckecks if the iframe has been clicked and pauses the video
    var monitor = setInterval(function () {
        var elem = document.activeElement;
        if (elem && elem.tagName == 'IFRAME') {
            clearInterval(monitor);
            element.style.display = 'block';
            document.getElementById(id).classList.remove('showVideo');
            let src = document.getElementById(id).src
            document.getElementById(id).src = src.replace('autoplay=1', 'autoplay=0');
        }
    }, 100);
}


// --------------- Code for showing video without watch more from youtube" ----------//
// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement("script");

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;

let fairnessID = '4bqrlZ-CyNs';

let transparencyID = 'q5CbK0Hs1pg';


function onYouTubeIframeAPIReady(videoId) {
    player = new YT.Player("player", {
        host: "https://www.youtube.com",
        /* no need to specify player
        size here since it is handled
        by the player-size div */
        videoId: videoId,
        playerVars: {
            enablejsapi: 1,
            playsinline: 1,
            start: 0,
            disablekb: 0
        },
        events: {
            onStateChange: onPlayerStateChange
        }
    });
}

function onPlayerStateChange(event) {
    console.log("player state: " + player.getPlayerState());
}

function updateVideoId() {
    let videoId = document.getElementById("videoId").value;
    player.loadVideoById(videoId, -1);
}

function stopVideo() {
    player.stopVideo();
}
