# GetDatumType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumType`

Gets the PMI datum type.
Gets the PMI datum type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumType() As System.Integer
```

```

Dim instance As IPMIDatumData
Dim value As System.Integer
 
value = instance.GetDatumType()
```

```

System.int GetDatumType()
```

```

System.int GetDatumType(); 
```

#### Return Value

PMI datum type as defined in [swPMIDatumType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumType_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.md)  
[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.md)  
[IPMIDatumData::GetDatumFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumFeature.md)  
[IPMIDatumData::GetDatumTarget Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumTarget.md)
