# IGetBasicColors Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetBasicColors`

Gets the basic colors in the color table.
Gets the basic colors in the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBasicColors( _
   ByVal ColorCount As System.Integer _
) As System.Integer
```

```

Dim instance As IColorTable
Dim ColorCount As System.Integer
Dim value As System.Integer
 
value = instance.IGetBasicColors(ColorCount)
```

```

System.int IGetBasicColors( 
   System.int ColorCount
)
```

```

System.int IGetBasicColors( 
   System.int ColorCount
) 
```

#### Parameters

*ColorCount*
:   Number of basic colors

#### Return Value

- in-process, unmanaged C++: Pointer to an array of basic colors of size ColorCount

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IColorTable::GetBasicColorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::GetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColors.md)  
[IColorTable::IGetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.md)
