# GetColorRefAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetColorRefAtIndex`

Gets the COLORREF at the specified index position of the color table.
Gets the COLORREF at the specified index position of the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColorRefAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IColorTable
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetColorRefAtIndex(Index)
```

```

System.int GetColorRefAtIndex( 
   System.int Index
)
```

```

System.int GetColorRefAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index position of the desired color

#### Return Value

COLORREF at the specified index position

Example

[Get COLORREF Values of Standard User-interface Elements (C#)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm)  
[Get COLORREF Values of Standard User-interface Elements (VB.NET)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm)  
[Get COLORREF Values of Standard User-interface Elements (VBA)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.md)  
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.md)  
[IColorTable::SetColorRefAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetColorRefAtIndex.md)
