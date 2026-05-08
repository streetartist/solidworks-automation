# ITwoMemberCornerTreatmentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData`

Allows access to a two member corner treatment feature of a structure system.
Allows access to a two member corner treatment feature of a structure system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ITwoMemberCornerTreatmentFeatureData 
```

```

Dim instance As ITwoMemberCornerTreatmentFeatureData
```

```

public interface ITwoMemberCornerTreatmentFeatureData 
```

```

public interface class ITwoMemberCornerTreatmentFeatureData 
```

Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.md) is false.

A two member corner is the position in a structure system where two members intersect. You can assign one member as a trim tool and use it to add or remove material from the other member. The trim tool member may be assigned to either member in a planar or body trim type.

In the SOLIDWORKS user interface, the Two member Corner PropertyManager contains three lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.md)
- [Corner group members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.md)
- [Miter trim plane point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~MiterTrimPlanePoint.md)

For more information, see:

- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Corner Management**
- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Two Member PropertyManager**

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
