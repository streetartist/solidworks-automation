# Position Property (ITableAnchor)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor~Position`

Gets or sets the location of the table anchor.
Gets or sets the location of the table anchor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As System.Object
```

```

Dim instance As ITableAnchor
Dim value As System.Object
 
instance.Position = value
 
value = instance.Position
```

```

System.object Position {get; set;}
```

```

property System.Object^ Position {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of doubles of x and y coordinates of the table anchor

Example

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)  
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)  
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnchor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.md)  
[ITableAnchor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.md)
