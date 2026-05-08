# GetDatumFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumFeature`

Gets the PMI datum feature.
Gets the PMI datum feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumFeature() As System.Object
```

```

Dim instance As IPMIDatumData
Dim value As System.Object
 
value = instance.GetDatumFeature()
```

```

System.object GetDatumFeature()
```

```

System.Object^ GetDatumFeature(); 
```

#### Return Value

[IPMIDatumFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.md)

Remarks

This method is valid only if [IPMIDatumData::GetDatumType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData~GetDatumType.md) returns [swPMIDatumType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumType_e.html).swPMIDatumType\_DatumFeature.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.md)  
[IPMIDatumData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.md)
