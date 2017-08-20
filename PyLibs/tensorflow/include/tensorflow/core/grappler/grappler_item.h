/* Copyright 2017 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_GRAPPLER_GRAPPLER_ITEM_H_
#define TENSORFLOW_GRAPPLER_GRAPPLER_ITEM_H_

#include <memory>
#include <string>
#include <utility>
#include <vector>

#include "tensorflow/core/framework/graph.pb.h"
#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/framework/variable.pb.h"
#include "tensorflow/core/protobuf/queue_runner.pb.h"

namespace tensorflow {
namespace grappler {

// A TensorFlow model to optimize.
// Models are represented by the combination of a graph, one of more fetch
// nodes, and potentially a set of nodes to feed.
// TODO(volunteer_needed): turn this struct into a class.
struct GrapplerItem {
  string id;  // A unique id for this item

  // Inputs
  GraphDef graph;
  std::vector<std::pair<string, Tensor>> feed;
  std::vector<string> fetch;

  // Initialization op(s).
  std::vector<string> init_ops;
  // Expected initialization time in seconds, or 0 if unknown
  int64 expected_init_time = 0;

  // Queue runner(s) required to run the queue(s) of this model.
  std::vector<QueueRunnerDef> queue_runners;

  // Return the set of node evaluated during a regular train/inference step.
  std::vector<const NodeDef*> MainOpsFanin() const;
  // Return the set of node run to populate the queues (if any).
  std::vector<const NodeDef*> EnqueueOpsFanin() const;
  // Return the set nodes used by TensorFlow to initialize the graph.
  std::vector<const NodeDef*> InitOpsFanin() const;
  // Return the set of variables accessed during a regular train/inference step.
  std::vector<const NodeDef*> MainVariables() const;
};

// Return the transitive fanin of a set of terminal nodes.
std::vector<const NodeDef*> ComputeTransitiveFanin(
    const GraphDef& graph, const std::vector<string>& terminal_nodes);

}  // end namespace grappler
}  // end namespace tensorflow

#endif  // TENSORFLOW_GRAPPLER_GRAPPLER_ITEM_H_
