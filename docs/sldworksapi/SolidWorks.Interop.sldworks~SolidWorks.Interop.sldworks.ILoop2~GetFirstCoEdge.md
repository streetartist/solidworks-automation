# GetFirstCoEdge Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge`

Gets the first coedge of the loop.
Gets the first coedge of the loop.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstCoEdge() As System.Object
```

```

Dim instance As ILoop2
Dim value As System.Object
 
value = instance.GetFirstCoEdge()
```

```

System.object GetFirstCoEdge()
```

```

System.Object^ GetFirstCoEdge(); 
```

#### Return Value

First [coedge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md) in loop

Remarks

The [ICoEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md) objects are returned in a CW or CCW manner based on the direction of the [ILoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md).

The loop direction is determined as follows: if a loop is viewed along its direction, with the face normal pointing upwards, then the face that owns the loop is to the left. This means that inner loops are CW and outer loops are CCW. To determine if a loop is an outer loop, see [ILoop2::IsOuter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter.md).

The coedge direction always aligns with the direction of the loop.

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::EnumCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~EnumCoEdges.md)  
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.md)  
[ILoop2::GetCoEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdgeCount.md)  
[ILoop2::GetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetCoEdges.md)  
[ILoop2::IGetCoEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetCoEdges.md)
