# IsSheetMetal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSheetMetal`

Gets whether this body was created by a sheet metal feature.
Gets whether this body was created by a sheet metal feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsSheetMetal() As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
value = instance.IsSheetMetal()
```

```

System.bool IsSheetMetal()
```

```

System.bool IsSheetMetal(); 
```

#### Return Value

True if this body was created by a sheet metal feature, false if not

Remarks

This method returns false for sheet metal bodies that are obtained from lightweight components using [IComponent2::GetBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
