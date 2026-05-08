# AddHole Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~AddHole`

Adds holes to this hole table.
Adds holes to this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddHole() As System.Integer
```

```

Dim instance As IHoleTable
Dim value As System.Integer
 
value = instance.AddHole()
```

```

System.int AddHole()
```

```

System.int AddHole(); 
```

#### Return Value

Number of holes added to this hole table

Remarks

You must either interactively or programmatically select the holes to add to the hole table before running this method.

|  |  |
| --- | --- |
| **To add holes...** | **Then...** |
| Interactively | - Select an edge that defines a hole to add that hole to this hole table. - Select a face that contains the holes that you want to add to this hole table. |
| Programatically | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md). |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)
