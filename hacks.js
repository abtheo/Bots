function check_same_clicks(event) {
  if (event.target.classList.contains('not-count')) {
    return
  }
  $(event.target).off('click', check_same_clicks);

  // Fix to avoid double counting clicks on blue and red buttons. Some issue with bubbling or so...
  // if you can do it better - you're welcome
  // if (["choice1", "choice2"].indexOf(event.target.id) !== -1) {
  //   return
  // }
  let click_x = event.pageX;
  let click_y = event.pageY;

  mouse_clicks.push([click_x, click_y]);
  if (last_click_time !== null) {
    click_intervals.push(Math.trunc(event.timeStamp - last_click_time))
  }
  last_click_time = event.timeStamp;
  if (mouse_clicks.length < CLICKS_COUNT) {} else {
    let all_clicks_average = get_all_clicks_distance_average();
    if (all_clicks_average < CLICKS_SENSITIVITY) {
      send_mouse_data('clicks_in_one_place_all', mouse_clicks);
      bot_mouse_triggered = true;
    } else {
      let pair_clicks_average = get_click_pairs_distance_average();
      if (pair_clicks_average < CLICKS_SENSITIVITY) {
        bot_mouse_triggered = true;
        send_mouse_data('clicks_in_one_place_pairs', mouse_clicks);
      } else {
        if (mouse_clicks.equals(prev_mouse_clicks)) {
          bot_mouse_triggered = true;
          send_mouse_data('clicks_in_one_place_sequence', mouse_clicks);
        } else {
          if (check_all_clicks_interval()) {
            bot_mouse_triggered = true;
            send_mouse_data('clicks_in_one_interval', click_intervals);
          } else {
            if (check_zero_coordinates()) {
              bot_mouse_triggered = true;
              send_mouse_data('clicks_at_zero_point', mouse_clicks);
            } else {
              send_mouse_data('good_user_clicks', mouse_clicks)
            }
          }
        }
      }
    }
    prev_mouse_clicks = mouse_clicks;
    mouse_clicks = [];
    click_intervals = [];
  }
}