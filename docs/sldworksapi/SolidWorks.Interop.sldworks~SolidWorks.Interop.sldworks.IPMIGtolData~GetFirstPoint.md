# GetFirstPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFirstPoint`

Gets the label of the first point for tolerances applied between two points or entities in this PMI Gtol.
Gets the label of the first point for tolerances applied between two points or entities in this PMI Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstPoint() As System.String
```

```

Dim instance As IPMIGtolData
Dim value As System.String
 
value = instance.GetFirstPoint()
```

```

System.string GetFirstPoint()
```

```

System.String^ GetFirstPoint(); 
```

#### Return Value

Label of the first point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.md)  
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.md)  
[IPMIGtolData::GetSecondPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetSecondPoint.md)
