# ISimpleCornerTreatmentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData`

Allows access to a simple corner treatment feature of a structure system.
Allows access to a simple corner treatment feature of a structure system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISimpleCornerTreatmentFeatureData 
```

```

Dim instance As ISimpleCornerTreatmentFeatureData
```

```

public interface ISimpleCornerTreatmentFeatureData 
```

```

public interface class ISimpleCornerTreatmentFeatureData 
```

Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.md) is false.

A simple corner is the position in a structure system where the ends of two members meet either in a body trim or a planar trim fashion.

In the SOLIDWORKS user interface, the Simple Corner PropertyManager contains two lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.md)
- [User defined trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~UserDefinedTrimFaces.md) faces

For more information, see:

- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Corner Management > Editing Simple Corners**
- **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Simple Corner PropertyManager**

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
