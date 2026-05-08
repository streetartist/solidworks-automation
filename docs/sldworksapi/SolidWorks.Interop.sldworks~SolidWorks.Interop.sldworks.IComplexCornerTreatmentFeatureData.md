# IComplexCornerTreatmentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData`

Allows access to a complex corner treatment feature of a structure system.
Allows access to a complex corner treatment feature of a structure system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IComplexCornerTreatmentFeatureData 
```

```

Dim instance As IComplexCornerTreatmentFeatureData
```

```

public interface IComplexCornerTreatmentFeatureData 
```

```

public interface class IComplexCornerTreatmentFeatureData 
```

Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.md) is false.

A complex corner is the position in a structure system where three or more members intersect.

In the SOLIDWORKS user interface, the Complex Corner PropertyManager contains five lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.md)
- [Trim tool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.md) member
- [Body trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetBodyTrimMembers.md) members
- [Planar trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.md) members
- [User defined trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~UserDefinedTrimFaces.md) faces

You can assign one member as a trim tool and use it to add or remove material from adjacent members. Other members are trimmed based on their designated trim orders and positions with respect to touching members.

For more information, see:

- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Corner Management > Trimming Complex Corners**
- ****SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Corner Management > Examples of Complex Corner Management****
- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Complex Corner PropertyManager**

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
