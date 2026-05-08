# GetConcentricAlignmentType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType`

Gets the alignment type of this mate.
Gets the alignment type of this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConcentricAlignmentType() As System.Integer
```

```

Dim instance As IMate2
Dim value As System.Integer
 
value = instance.GetConcentricAlignmentType()
```

```

System.int GetConcentricAlignmentType()
```

```

System.int GetConcentricAlignmentType(); 
```

#### Return Value

Alignment type as defined in [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::SetConcentricAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetConcentricAlignmentType.md)  
[IMate2::GetCurrentMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetCurrentMisalignedDeviation.md)  
[IMate2::GetMaximumMisalignedDeviation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.md)
