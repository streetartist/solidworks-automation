# IMate2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members`

Allows access to various assembly mate parameters.
The following tables list the members exposed by [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Alignment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Alignment.md) | Gets the type of alignment for this mate. |
| Property | [CanBeFlipped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~CanBeFlipped.md) | Gets whether this distance or angle mate can be flipped. |
| Property | [DisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension.md) | Obsolete. Superseded by [IMate2::DisplayDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.md). |
| Property | [DisplayDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DisplayDimension2.md) | Gets the specified display dimension for this mate. |
| Property | [DistanceFirstArcCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.md) | Gets the the first arc condition of this distance mate between cylindrical components. |
| Property | [DistanceSecondArcCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.md) | Gets the the second arc condition of this distance mate between cylindrical components. |
| Property | [Flipped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Flipped.md) | Gets or sets whether to flip the distance or angle mate. |
| Property | [HasLoadBearingFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.md) | Gets whether this mate has load bearing faces. |
| Property | [HasTreatInterferenceAsShrinkFit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasTreatInterferenceAsShrinkFit.md) | Gets whether interference in this mate is treated as shrink/press fit. |
| Property | [IsLoadBearingFacesBonded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.md) | Get whether the load bearing faces of this mate are bonded. |
| Property | [LockMagneticMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~LockMagneticMate.md) | Gets or sets whether to lock this magnetic mate. |
| Property | [MateLoadReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateLoadReference.md) | Gets the mate load reference associated with this mate. |
| Property | [MaximumVariation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MaximumVariation.md) | Gets the maximum variation, in meters or radians, for the dimension of this distance or angle mate. |
| Property | [MinimumVariation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MinimumVariation.md) | Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.md) | Gets the type of mate. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [ForceMisalignment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~ForceMisalignment.md) | Forces a misaligned mate condition for this concentric mate. |
| Method | [GetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.md) | Gets the alignment type of this mate. |
| Method | [GetCurrentMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.md) | Gets the current misalignment deviation for the misaligned concentric mate. |
| Method | [GetForce](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetForce.md) | Gets the magnitude and direction of the force applied to this mate. |
| Method | [GetLinkedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetLinkedMate.md) | Gets the linked mate of this concentric mate. |
| Method | [GetMateEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMateEntityCount.md) | Gets the number of entities for this mate. |
| Method | [GetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.md) | Gets the maximum allowed misalignment deviation for this misaligned concentric mate. |
| Method | [GetSupplementalFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetSupplementalFaces.md) | Gets the faces in this mate. |
| Method | [GetTorque](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetTorque.md) | Gets the angle and the axis of the torque applied to this mate. |
| Method | [GetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty.md) | Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate. |
| Method | [IGetSupplementalFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IGetSupplementalFaces.md) | Gets the faces in this mate. |
| Method | [MateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity.md) | Gets an entity associated with a mate. |
| Method | [RemoveMisalignment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~RemoveMisalignment.md) | Removes the misaligned mate condition of this concentric mate. |
| Method | [SetConcentricAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetConcentricAlignmentType.md) | Sets the alignment type of this mate. |
| Method | [SetForce](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetForce.md) | Sets the magnitude and direction of the force to apply to this mate. |
| Method | [SetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetMaximumMisalignedDeviation.md) | Sets the maximum allowed misalignment deviation for this misaligned concentric mate. |
| Method | [SetTorque](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetTorque.md) | Sets the angle and the axis of the torque to apply to this mate. |
| Method | [SetUseMisalignedDeviationDocumentProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.md) | Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate. |

[Top](#top)

 

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)  
[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)
