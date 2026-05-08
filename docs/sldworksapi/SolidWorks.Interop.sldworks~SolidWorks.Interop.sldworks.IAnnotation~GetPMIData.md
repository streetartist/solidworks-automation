# GetPMIData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData`

Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation.
Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPMIData() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetPMIData()
```

```

System.object GetPMIData()
```

```

System.Object^ GetPMIData(); 
```

#### Return Value

[IPMIDatumData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData.md), [IPMIDimensionData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.md), [IPMIGtolData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.md); null if no PMI data is associated with this annotation (see **Remarks**)

Remarks

Use [IAnnotation::GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.md) to determine the feature data object returned by this method.

Example

[Get PMI Data (VBA)](Get_PMI_Data_Example_VB.htm)  
[Get PMI Data (C#)](Get_PMI_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
