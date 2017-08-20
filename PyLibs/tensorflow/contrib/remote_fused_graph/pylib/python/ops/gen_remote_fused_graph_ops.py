"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections as _collections

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2

# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library

def remote_fused_graph_execute(inputs, Toutputs,
                               serialized_remote_fused_graph_execute_info,
                               name=None):
  r"""Execute a sub graph on a remote processor.

  The graph specifications(such as graph itself, input tensors and output names)
  are stored as a serialized protocol buffer of RemoteFusedGraphExecuteInfo
  as serialized_remote_fused_graph_execute_info.
  The specifications will be passed to a dedicated registered
  remote fused graph executor.  The executor will send the graph specifications
  to a remote processor and execute that graph.  The execution results
  will be passed to consumer nodes as outputs of this node.

  Args:
    inputs: A list of `Tensor` objects.
      Arbitrary number of tensors with arbitrary data types
    Toutputs: A list of `tf.DTypes`.
    serialized_remote_fused_graph_execute_info: A `string`.
      Serialized protocol buffer
      of RemoteFusedGraphExecuteInfo which contains graph specifications.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Toutputs`.
    Arbitrary number of tensors with arbitrary data types
  """
  result = _op_def_lib.apply_op("RemoteFusedGraphExecute", inputs=inputs,
                                Toutputs=Toutputs,
                                serialized_remote_fused_graph_execute_info=serialized_remote_fused_graph_execute_info,
                                name=name)
  return result


def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib


# op {
#   name: "RemoteFusedGraphExecute"
#   input_arg {
#     name: "inputs"
#     type_list_attr: "Tinputs"
#   }
#   output_arg {
#     name: "outputs"
#     type_list_attr: "Toutputs"
#   }
#   attr {
#     name: "Tinputs"
#     type: "list(type)"
#     has_minimum: true
#   }
#   attr {
#     name: "Toutputs"
#     type: "list(type)"
#     has_minimum: true
#   }
#   attr {
#     name: "serialized_remote_fused_graph_execute_info"
#     type: "string"
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\252\001\n\027RemoteFusedGraphExecute\022\021\n\006inputs2\007Tinputs\032\023\n\007outputs2\010Toutputs\"\027\n\007Tinputs\022\nlist(type)(\001\"\030\n\010Toutputs\022\nlist(type)(\001\"4\n*serialized_remote_fused_graph_execute_info\022\006string")
