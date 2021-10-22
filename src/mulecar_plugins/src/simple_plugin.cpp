#include "simple.hpp"

namespace gazebo
{
  void Simple::Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
  {
    // Store the pointer to the model
    this->model = _parent;
    gzdbg << "hello debug msg" << std::endl;
    gzmsg << "hello info msg" << std::endl;
    gzwarn << "hello warning msg" << std::endl;
    gzerr << "hello error msg" << std::endl;

    // Listen to the update event. This event is broadcast every
    // simulation iteration.
    this->updateConnection = event::Events::ConnectWorldUpdateBegin(
        std::bind(&Simple::OnUpdate, this));
  }

  // Called by the world update start event
  void Simple::OnUpdate(){
    this->model->SetLinearVel(ignition::math::Vector3d(.3, 0, 0));
  }

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(Simple)
}