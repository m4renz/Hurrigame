import pulsectl

with pulsectl.Pulse('general-info') as pulse:
    print("Sink List: ")
    print(pulse.sink_list())
    print("--------------")
    print("Sink Input List: ")
    print(pulse.sink_input_list())
    print("--------------")
    print("Source List: ")
    print(pulse.source_list())
    print("--------------")
    print("Default Sink: ")
    print(pulse.server_info().default_sink_name)
    print("--------------")

with pulsectl.Pulse('volume-increaser') as pulse:
  for sink in pulse.sink_list():
    # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
    print("Sink: " + sink.name)
    pulse.volume_change_all_chans(sink, -0.3)