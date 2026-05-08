# GetUseMisalignedDeviationDocumentProperty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetUseMisalignedDeviationDocumentProperty`

Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate.
Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseMisalignedDeviationDocumentProperty() As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
value = instance.GetUseMisalignedDeviationDocumentProperty()
```

```

System.bool GetUseMisalignedDeviationDocumentProperty()
```

```

System.bool GetUseMisalignedDeviationDocumentProperty(); 
```

#### Return Value

True to use the document property value for maximum misalignment deviation, false to not

Remarks

If this method returns false, then the maximum deviation used is returned by [IMate2::GetMaximumMisalignedDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMaximumMisalignedDeviation.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::SetUseMisalignedDeviationDocumentProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetUseMisalignedDeviationDocumentProperty.md)
