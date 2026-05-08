# GetCustomColorCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount`

Gets the number of custom colors in the color table.
Gets the number of custom colors in the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCustomColorCount() As System.Integer
```

```

Dim instance As IColorTable
Dim value As System.Integer
 
value = instance.GetCustomColorCount()
```

```

System.int GetCustomColorCount()
```

```

System.int GetCustomColorCount(); 
```

#### Return Value

Number of custom colors

Remarks

Call this method before calling [IColorTable::IGetCustomColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::GetBasicColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.md)  
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.md)  
[IColorTable::GetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.md)  
[IColorTable:GetStandardCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.md)
