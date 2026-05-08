# IPMIDimensionData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData`

Allows access to the Product and Manufacturing Information (PMI) for a dimension annotation in a STEP 242 model.
Allows access to the Product and Manufacturing Information (PMI) for a dimension annotation in a STEP 242 model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPMIDimensionData 
```

```

Dim instance As IPMIDimensionData
```

```

public interface IPMIDimensionData 
```

```

public interface class IPMIDimensionData 
```

Remarks

This interface is valid only if [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.md) returns [swPMIType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPMIType_e.html).swPMIType\_Dimension.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.md)  
[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.md)
