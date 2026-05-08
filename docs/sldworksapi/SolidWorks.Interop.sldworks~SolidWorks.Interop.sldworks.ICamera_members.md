# ICamera Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members`

Allows access to the camera feature.
The following tables list the members exposed by [ICamera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~AspectRatio.md) | Gets the aspect ratio (width/height) of the field of view rectangle for the camera.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [DepthOfFieldEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldEnabled.md) | Gets whether depth of field effects are enabled or disabled.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [DepthOfFieldOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldOffset.md) | Gets the approximate distance from the camera's focal plane to point where focus is lost.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [FieldOfViewAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.md) | Gets the camera's horizontal angle of the field of view.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [FieldOfViewDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth.md) | Gets the camera's depth of the field of view.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [FieldOfViewHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.md) | Gets the camera's height of the field of view.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [ID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~ID.md) | Gets the ID for this camera. |
| Property | [LockCameraPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.md) | Gets or sets whether the camera position is locked. |
| Property | [Perspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective.md) | Gets whether the camera is in perspective mode or not.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Pitch.md) | Gets or sets the pitch (up or down angle) of a [floating camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type.md). |
| Property | [PositionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.md) | Gets or sets the camera position type. |
| Property | [RotationRollAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.md) | Gets or sets the camera's roll angle. |
| Property | [RotationRollBySelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.md) | Gets or sets whether you can select the camera's rotation roll direction. |
| Property | [RotationRollEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.md) | Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction. |
| Property | [RotationRollFlipDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.md) | Gets or sets whether to flip the direction of the camera 180. |
| Property | [TargetPointBySelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.md) | Gets or sets whether you can set the target point. |
| Property | [TargetPointPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.md) | Gets or sets the position of the target point. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type.md) | Gets or sets the type of camera. |
| Property | [Yaw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Yaw.md) | Gets or sets the yaw (side-to-side angle) of a [floating camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type.md). |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetFocalDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetFocalDistance.md) | Gets the camera's focal distance. |
| Method | [GetPointOfInterestDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPointOfInterestDistance.md) | Gets the distance of the point of interest from the camera. |
| Method | [GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.md) | Gets the current position of the camera. |
| Method | [GetPositionCartesian](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.md) | Gets the Cartesian coordinates for the camera position. |
| Method | [GetPositionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.md) | Gets the entity to which the camera is attached. |
| Method | [GetPositionSpherical](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.md) | Gets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target. |
| Method | [GetTargetPointEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.md) | Gets the target point on the entity for the camera. |
| Method | [GetUpVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetUpVector.md) | Gets the camera's up direction. |
| Method | [GetViewVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetViewVector.md) | Gets the direction in which the camera is looking. |
| Method | [SetPositionCartesian](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.md) | Sets the Cartesian coordinates for the camera position. |
| Method | [SetPositionEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.md) | Sets the entity to which the camera is attached. |
| Method | [SetPositionSpherical](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.md) | Sets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target. |
| Method | [SetTargetPointEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.md) | Gets the target point on the entity for the camera. |

[Top](#top)

 

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
