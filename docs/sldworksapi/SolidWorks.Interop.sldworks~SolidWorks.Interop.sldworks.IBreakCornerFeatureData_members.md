# IBreakCornerFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members`

Allows access to a break corner feature.
The following tables list the members exposed by [IBreakCornerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [BreakType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~BreakType.md) | Gets or sets the break corner type. |
| Property | [CenteredOnBendLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~CenteredOnBendLines.md) | Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature. |
| Property | [Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Distance.md) | Gets or sets the chamfer length or fillet radius, depending on the break corner type. |
| Property | [Entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Entities.md) | Gets or sets the faces or edges to which this break corner is applied. |
| Property | [InternalCornersOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~InternalCornersOnly.md) | Gets or sets whether to add or subtract material from break corner/corner trim features. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~AccessSelections.md) | Gains access to the selections that describe this break corner feature. |
| Method | [GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~GetEntitiesCount.md) | Gets the number of faces or edges associated with this break corner feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IAccessSelections.md) | Gains access to the selections that describe this break corner feature. |
| Method | [IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.md) | Gets the faces or edges to which this break corner is applied. |
| Method | [ISetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~ISetEntities.md) | Sets the faces or edges to which this break corner is applied. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~ReleaseSelectionAccess.md) | Releases access to selections for this break corner feature. |

[Top](#top)

 

See Also

#### Reference

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertSheetMetalCornerTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalCornerTrim.md)  
[IModelDoc2::InsertSheetMetalBreakCorner Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalBreakCorner.md)
