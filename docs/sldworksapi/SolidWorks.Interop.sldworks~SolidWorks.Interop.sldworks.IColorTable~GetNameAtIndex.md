# GetNameAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetNameAtIndex`

Gets the name of the color at the specified index position in the color table.
Gets the name of the color at the specified index position in the color table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNameAtIndex( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IColorTable
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetNameAtIndex(Index)
```

```

System.string GetNameAtIndex( 
   System.int Index
)
```

```

System.String^ GetNameAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index position of the desired color

#### Return Value

Name of the color at the specified index

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
