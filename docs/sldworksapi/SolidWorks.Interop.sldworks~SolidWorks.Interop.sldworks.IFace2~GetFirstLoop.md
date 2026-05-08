# GetFirstLoop Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop`

Gets the first loop in this face, which is not necessarily the outer loop.
Gets the first loop in this face, which is not necessarily the outer loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstLoop() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetFirstLoop()
```

```

System.object GetFirstLoop()
```

```

System.Object^ GetFirstLoop(); 
```

#### Return Value

First [loop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Loops (VBA)](Get_Loops_Example_VB.htm)  
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)  
[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)  
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

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md)  
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.md)  
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.md)  
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.md)
