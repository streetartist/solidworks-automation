# ISimulationMotorFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members`

Allows access to the data that defines linear or rotary motors in SOLIDWORKS Motion studies.
The following tables list the members exposed by [ISimulationMotorFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [DirectionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DirectionReference.md) | Gets or sets the direction in which the motor moves. |
| Property | [DriveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DriveType.md) | Sets the drive type of this motor feature. |
| Property | [Expression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.md) | Gets or sets the motor motion expression for this motor feature. |
| Property | [ExternalState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ExternalState.md) | Gets or sets whether your application can listen to motor-related motion study event. |
| Property | [InterpolationScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolationScheme.md) | Gets or set the interpolation scheme for this motor feature. |
| Property | [LoadReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadReferences.md) | Gets or sets the load references for this motor feature. |
| Property | [Location](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Location.md) | Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part. |
| Property | [Magnitude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Magnitude.md) | Get or set the magnitude for this motor feature. |
| Property | [MotionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~MotionType.md) | Gets or sets the type of motion of this motor feature. |
| Property | [MotorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~MotorType.md) | Gets the type of motor for this motor feature. |
| Property | [RelativeComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~RelativeComponent.md) | Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ReverseDirection.md) | Gets or sets whether or not to reverse the direction of the motor. |
| Property | [SplineData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~SplineData.md) | Gets or sets the spline data points for this motor feature. |
| Property | [Velocity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Velocity.md) | Gets or sets the speed of the motor if no other force acts on it. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [ConstantSpeedMotor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.md) | Sets the constant speed for this motor feature. |
| Method | [DistanceMotor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.md) | Sets the distance and time for which to operate this motor feature. |
| Method | [GetInterpolatedValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~GetInterpolatedValue.md) | Gets the interopolated value at the specified time for this motor feature. |
| Method | [InterpolatedMotor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.md) | Sets the drive type and interpolation scheme for this motor feature. |
| Method | [LoadSplineData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadSplineData.md) | Loads the spline data from the specified file for this motor feature. |
| Method | [OscillatingMotor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.md) | Sets the displacement and frequency for oscillating motion for this motor feature. |

[Top](#top)

 

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.md)  
[Simulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[SimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md)  
[SimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)
