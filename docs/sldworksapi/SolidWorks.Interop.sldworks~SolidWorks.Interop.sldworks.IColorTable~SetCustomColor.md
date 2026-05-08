# SetCustomColor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetCustomColor`

Sets a custom color.
Sets a custom color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCustomColor( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer _
) As System.Boolean
```

```

Dim instance As IColorTable
Dim Index As System.Integer
Dim ColorRef As System.Integer
Dim value As System.Boolean
 
value = instance.SetCustomColor(Index, ColorRef)
```

```

System.bool SetCustomColor( 
   System.int Index,
   System.int ColorRef
)
```

```

System.bool SetCustomColor( 
   System.int Index,
   System.int ColorRef
) 
```

#### Parameters

*Index*
:   Index of the custom color to set

*ColorRef*
:   COLORREF value

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::GetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.md)  
[IColorTable::IGetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.md)  
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.md)
