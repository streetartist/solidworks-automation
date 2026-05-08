# GetBasicColorCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount`

Gets the number of basic colors defined in the color table.
Gets the number of basic colors defined in the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBasicColorCount() As System.Integer
```

```

Dim instance As IColorTable
Dim value As System.Integer
 
value = instance.GetBasicColorCount()
```

```

System.int GetBasicColorCount()
```

```

System.int GetBasicColorCount(); 
```

#### Return Value

Number of basic colors

Remarks

Call this method before calling [IColorTable::IGetBasicColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetBasicColors.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::IGetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetBasicColors.md)  
[IColorTable::GetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColors.md)  
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.md)  
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.md)  
[IColorTable:GetStandardCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.md)
