# IsVisible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IsVisible`

Gets whether this BOM is visible.
Gets whether this BOM is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsVisible() As System.Boolean
```

```

Dim instance As IBomTable
Dim value As System.Boolean
 
value = instance.IsVisible()
```

```

System.bool IsVisible()
```

```

System.bool IsVisible(); 
```

#### Return Value

True if the BOM is visible, false if not

Remarks

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)
