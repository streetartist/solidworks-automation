# ISimulationForceFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members`

Allows access to a force or torque feature in SOLIDWORKS Motion studies.
The following tables list the members exposed by [ISimulationForceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [ActionDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionDirection.md) | Gets or sets the direction of the force. |
| Property | [ActionLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionLocation.md) | Gets or sets the location at which to apply the force for an action-only force. |
| Property | [ActionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ActionType.md) | Gets or sets the type of action for this Force feature. |
| Property | [ExternalState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ExternalState.md) | Gets or sets whether your application can listen to force-related motion study events. |
| Property | [ForceFunctionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceFunctionType.md) | Gets or sets the type of function for this Force feature. |
| Property | [ForceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ForceType.md) | Gets the type of force.  **NOTE: This property is a get-only property. Set is not implemented.** |
| Property | [FunctionConstantValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionConstantValue.md) | Gets or sets the function constant value for this Force feature. |
| Property | [FunctionExpression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionExpression.md) | Gets or sets the expression function for this Force feature. |
| Property | [FunctionInterpolatedValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.md) | Gets or sets the interpolated values for this Force feature. |
| Property | [InterpolationScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.md) | Gets the interopolation scheme for this Force feature. |
| Property | [LoadReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~LoadReferences.md) | Gets or sets the load references for this Force feature. |
| Property | [ReactionLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReactionLocation.md) | Gets or sets the location at which to apply the force for an action/reaction force. |
| Property | [ReferenceComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReferenceComponent.md) | Gets or sets the component to serve as a reference frame for the force. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReverseDirection.md) | Gets or sets whether to reverse the direction of the force. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetEndPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetEndPoints.md) | Gets the end points of this Force feature. |
| Method | [GetFunctionHarmonicValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionHarmonicValues.md) | Gets the harmonic function values for this Force feature. |
| Method | [GetFunctionStepValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetFunctionStepValues.md) | Gets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature. |
| Method | [GetInterpolatedValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.md) | Gets the interpolated value at the specified time for this Force feature. |
| Method | [LoadSplineData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~LoadSplineData.md) | Loads the spline data from the specified file for this Force feature. |
| Method | [SetEndPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetEndPoints.md) | Sets the end points for this Force feature. |
| Method | [SetFunctionHarmonicValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionHarmonicValues.md) | Sets the harmonic function values for this Force feature. |
| Method | [SetFunctionStepValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetFunctionStepValues.md) | Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature. |

[Top](#top)

 

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISimulationGravityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData.md)  
[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[Simulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[SimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md)  
[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)
