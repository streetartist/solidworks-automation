# GetTolTypeValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues`

Gets the tolerance zone values in this PMI Gtol frame box.
Gets the tolerance zone values in this PMI Gtol frame box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTolTypeValues() As System.Object
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Object
 
value = instance.GetTolTypeValues()
```

```

System.object GetTolTypeValues()
```

```

System.Object^ GetTolTypeValues(); 
```

#### Return Value

Array of tolerance zone values

Remarks

The array returned by this method maps one-to-one and onto with the array returned by [IPMIGtolBoxData::GetTolTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypes.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)  
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.md)
