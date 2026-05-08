# TableAnchor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TableAnchor`

Gets the specified table anchor.
Gets the specified table anchor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property TableAnchor( _
   ByVal TableType As System.Integer _
) As TableAnchor
```

```

Dim instance As ISheet
Dim TableType As System.Integer
Dim value As TableAnchor
 
value = instance.TableAnchor(TableType)
```

```

TableAnchor TableAnchor( 
   System.int TableType
) {get;}
```

```

property TableAnchor^ TableAnchor {
   TableAnchor^ get(System.int TableType);
}
```

#### Parameters

*TableType*
:   Table type as defined in [swTableAnnotationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)

#### Property Value

[Table anchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md)

Example

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)  
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)  
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::SetAsTableAnchor Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetAsTableAnchor.md)
