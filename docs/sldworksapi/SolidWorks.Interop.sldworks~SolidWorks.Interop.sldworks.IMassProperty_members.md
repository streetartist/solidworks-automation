# IMassProperty Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members`

Obsolete. Superseded by IMassProperty2.
The following tables list the members exposed by [IMassProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.md) | Gets the center of mass. |
| Property | [Density](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Density.md) | Gets the density for this model. |
| Property | [Mass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.md) | Gets the mass of this model. |
| Property | [OverrideCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.md) | Gets or sets whether to override the calculated center of mass value for the model. |
| Property | [OverrideMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.md) | Gets or sets whether to override the calculated mass value for the model. |
| Property | [OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.md) | Gets or sets whether to override the calculated moments of inertia for the model. |
| Property | [PrincipleAxesOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.md) | Gets the principal axes of inertia for this model. |
| Property | [PrincipleMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.md) | Gets the principal moments of inertia for this model. |
| Property | [SurfaceArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SurfaceArea.md) | Gets the surface area for this model. |
| Property | [UserAssigned](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UserAssigned.md) | Gets whether the mass property values are user-defined or calculated for this document, regardless of which model is being edited. |
| Property | [UseSystemUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UseSystemUnits.md) | Gets and sets whether to use system units or document units when calculating mass properties for this model. |
| Property | [Volume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Volume.md) | Gets the volume of this model. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~AddBodies.md) | Uses only the specified bodies when calculating the mass properties for this model. |
| Method | [GetMomentOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.md) | Gets the moment of inertia at the specified coordinate system for this model. |
| Method | [IAddBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IAddBodies.md) | Uses only the specified bodies when calculating the mass properties for this model. |
| Method | [IGetCenterOfMass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetCenterOfMass.md) | Gets the center of mass for this model. |
| Method | [IGetMomentOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.md) | Gets the moment of inertia at the specified coordinate system for this model. |
| Method | [IGetPrincipleAxesOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.md) | Gets the principal axes of inertia for this model. |
| Method | [IGetPrincipleMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.md) | Gets the principal moments of inertia for this model. |
| Method | [ISetAssignedMassProp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.md) | Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document. |
| Method | [ISetOverrideCenterOfMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.md) | Overrides the center of mass of the model currently being edited in this part or assembly document. |
| Method | [ISetOverrideMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMassValue.md) | Overrides the mass of the model currently being edited in this part or assembly document. |
| Method | [ISetOverrideMomentsOfInertiaValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMomentsOfInertiaValue.md) | Overrides the moments of inertia of the model currently being edited in this part or assembly document. |
| Method | [ISetOverridePrincipleAxesOrientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation.md) | Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document. |
| Method | [ISetOverridePrincipleMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleMomentsOfInertia.md) | Overrides the principal moments of inertia of the model currently being edited in this part or assembly document. |
| Method | [SetAssignedMassProp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp.md) | Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document. |
| Method | [SetCoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetCoordinateSystem.md) | Sets the coordinate system to use when calculating mass properties for this model. |
| Method | [SetOverrideCenterOfMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.md) | Overrides the center of mass of the model currently being edited in this part or assembly document. |
| Method | [SetOverrideMassValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMassValue.md) | Overrides the mass of the model currently being edited in this part or assembly document. |
| Method | [SetOverrideMomentsOfInertiaValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMomentsOfInertiaValue.md) | Overrides the moments of inertia of the model currently being edited in this part or assembly document. |
| Method | [SetOverridePrincipleAxesOrientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation.md) | Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document. |
| Method | [SetOverridePrincipleMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleMomentsOfInertia.md) | Overrides the principal moments of inertia of the model currently being edited in this part or assembly document. |

[Top](#top)

 

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::GetMassProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.md)
