function HAR_button_start() {
    $.post($SCRIPT_ROOT + '/start_har')
    .done(handle_response)
    .fail(handle_error)
  }

  function HAR_button_stop() {
    $.post($SCRIPT_ROOT + '/stop_har')
    .done(handle_response)
    .fail(handle_error)
  }

function BP_mapping_button_start() {
    $.post($SCRIPT_ROOT + '/start_bpm')
    .done(handle_response)
    .fail(handle_error)
  }

  function BP_mapping_button_stop() {
    $.post($SCRIPT_ROOT + '/stop_bpm')
    .done(handle_response)
    .fail(handle_error)
  }

  function CC_button_start() {
    $.post($SCRIPT_ROOT + '/start_occ')
    .done(handle_response)
    .fail(handle_error)
  }

  function CC_button_stop() {
    $.post($SCRIPT_ROOT + '/stop_occ')
    .done(handle_response)
    .fail(handle_error)
  }

  function All_button_start() {
    $.post($SCRIPT_ROOT + '/start_all')
    .done(handle_response)
    .fail(handle_error)
  }

  function All_button_stop() {
    $.post($SCRIPT_ROOT + '/stop_all')
    .done(handle_response)
    .fail(handle_error)
  }

  function DP_button_start() {
    $.post($SCRIPT_ROOT + '/start_dp')
    .done(handle_response)
    .fail(handle_error)
  }

  function DP_button_stop() {
    $.post($SCRIPT_ROOT + '/stop_dp')
    .done(handle_response)
    .fail(handle_error)
  } 

  // ############################################
  // ------------ Handling Functions ------------
  // ############################################

  function handle_error(error) {
    toastr.error(error.responseJSON.message, 'Error in ' + error.responseJSON.source, {positionClass:'toast-top-center'})
  }

  function handle_response(response) {
    toastr.success('Successfully finished executing ' + response.source, 'Success', {positionClass:'toast-top-center'})
  }