#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>

#ifndef SIMPLE_PLUGIN_HPP_
#define SIMPLE_PLUGIN_HPP_


namespace gazebo
{
    class Simple : public ModelPlugin
    {
    public:
        void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/);
        void OnUpdate();

        // Pointer to the model
    private:
        gazebo::physics::ModelPtr model;
        gazebo::event::ConnectionPtr updateConnection;
    };
}
#endif