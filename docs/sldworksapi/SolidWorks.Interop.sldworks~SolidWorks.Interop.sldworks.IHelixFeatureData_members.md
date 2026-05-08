# IHelixFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members`

Allows access to a helix feature.
The following tables list the members exposed by [IHelixFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Clockwise](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Clockwise.md) | Gets or sets the direction of the turns of this helix feature. |
| Property | [DefinedBy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy.md) | Gets or sets the definition of this helix feature. |
| Property | [Height](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Height.md) | Gets or sets the height of this helix feature. |
| Property | [Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Pitch.md) | Gets or sets the pitch of this helix feature. |
| Property | [PitchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.md) | Gets the number of regions in this variable-pitch helix. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~ReverseDirection.md) | Gets or sets whether to make this helix feature extend backward from the point of origin. |
| Property | [Revolution](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Revolution.md) | Gets or sets the number of revolutions for this helix feature. |
| Property | [StartingAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~StartingAngle.md) | Gets or sets the angle for the first turn of this helix feature. |
| Property | [Taper](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Taper.md) | Gets or sets whether this constant-pitch helix feature is tapered. |
| Property | [TaperAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~TaperAngle.md) | Gets or sets the angle of the taper for this constant-pitch helix feature. |
| Property | [TaperOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~TaperOutward.md) | Gets or sets the direction of the taper for this constant-pitch helix feature. |
| Property | [VariablePitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.md) | Gets whether this helix feature has a variable or constant pitch. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddLastRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.md) | Adds a region to the end of the Region parameters table of this variable-pitch helix. |
| Method | [DeleteRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.md) | Deletes the specified records in the Region parameters table of this variable-pitch helix. |
| Method | [GetRegionParameterAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.md) | Gets the specified parameter value for the specified region in this variable-pitch helix. |
| Method | [InsertRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.md) | Inserts a record before the specified index in the Region parameters table of this variable-pitch helix. |
| Method | [SetRegionParameterAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.md) | Sets the specified parameter for the specified region in this variable-pitch helix. |

[Top](#top)

 

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDoc2::InsertHelix Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHelix.md)  
[IFeatureManager::InsertVariablePitchHelix Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.md)  
[IFeatureManager::AddVariablePitchHelixFirstPitchAndDiameter Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.md)  
[IFeatureManager::AddVariablePitchHelixSegment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.md)  
[IFeatureManager::EndVariablePitchHelix Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.md)
