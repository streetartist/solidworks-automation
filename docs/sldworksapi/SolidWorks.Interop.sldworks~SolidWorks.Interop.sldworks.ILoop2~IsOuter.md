# IsOuter Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter`

Indicates whether the loop is the outermost loop on the face.
Indicates whether the loop is the outermost loop on the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsOuter() As System.Boolean
```

```

Dim instance As ILoop2
Dim value As System.Boolean
 
value = instance.IsOuter()
```

```

System.bool IsOuter()
```

```

System.bool IsOuter(); 
```

#### Return Value

True if the loop is the outermost loop, false if not

Remarks

Some situations exist where no clear outer loop is defined. For example, the cylindrical face of an extruded circle has two loops that could be considered outer loops.

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Loops (VBA)](Get_Loops_Example_VB.htm)  
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)  
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)  
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)
