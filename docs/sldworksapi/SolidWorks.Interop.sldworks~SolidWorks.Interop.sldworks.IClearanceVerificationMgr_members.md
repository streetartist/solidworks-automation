# IClearanceVerificationMgr Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members`

Allows you to check the clearance between selected components and/or faces in assemblies.
The following tables list the members exposed by [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CheckClearanceBetween](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CheckClearanceBetween.md) | Gets or sets the type of clearance check: between selected items or between selected items and the rest of the assembly. |
| Property | [IgnoreClearanceEqualToSpecifiedValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.md) | Gets or sets whether to ignore clearances equal to or greater than [IClearanceVerificationMgr::GetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetMinimumAcceptableClearance.md). |
| Property | [TreatSubAssembliesAsComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~TreatSubAssembliesAsComponents.md) | Gets or sets whether to treat subassemblies as single components for clearance verification. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CalculateClearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CalculateClearances.md) | Runs a clearance check of selected assembly components and/or faces. |
| Method | [GetComponentsOrFacesToCheck](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetComponentsOrFacesToCheck.md) | Gets the components and/or faces for which to check clearance. |
| Method | [GetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetMinimumAcceptableClearance.md) | Gets the minimum acceptable clearance value. |
| Method | [SetComponentsOrFacesToCheck](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetComponentsOrFacesToCheck.md) | Sets the components or faces for which to check clearances. |
| Method | [SetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance.md) | Sets the minimum acceptable clearance value. |

[Top](#top)

 

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.md)
