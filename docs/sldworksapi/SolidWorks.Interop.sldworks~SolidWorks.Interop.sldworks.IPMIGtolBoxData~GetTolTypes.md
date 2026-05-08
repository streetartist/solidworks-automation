# GetTolTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypes`

Gets the tolerance zone types in this PMI Gtol frame box.
Gets the tolerance zone types in this PMI Gtol frame box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTolTypes() As System.Object
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Object
 
value = instance.GetTolTypes()
```

```

System.object GetTolTypes()
```

```

System.Object^ GetTolTypes(); 
```

#### Return Value

Array of tolerance zone types as defined in [swGtolTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolTolType_e.html)

Remarks

The tolerance zone types returned by this method map on-to-one and onto with tolerance zone values returned by [IPMIGtolBoxData::GetTolTypeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)
