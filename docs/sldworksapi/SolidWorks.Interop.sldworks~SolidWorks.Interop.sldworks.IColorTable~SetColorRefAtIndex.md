# SetColorRefAtIndex Method (IColorTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetColorRefAtIndex`

Sets the specified color value within the color table.
Sets the specified color value within the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetColorRefAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer, _
   ByVal ApplyTo As System.Integer _
) 
```

```

Dim instance As IColorTable
Dim Index As System.Integer
Dim ColorRef As System.Integer
Dim ApplyTo As System.Integer
 
instance.SetColorRefAtIndex(Index, ColorRef, ApplyTo)
```

```

void SetColorRefAtIndex( 
   System.int Index,
   System.int ColorRef,
   System.int ApplyTo
)
```

```

void SetColorRefAtIndex( 
   System.int Index,
   System.int ColorRef,
   System.int ApplyTo
) 
```

#### Parameters

*Index*
:   Index value within the color table you want to modify

*ColorRef*
:   COLORREF value

*ApplyTo*
:   Not used; specify 0

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::GetColorRefAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetColorRefAtIndex.md)
