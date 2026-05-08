# FaceInSurfaceSense Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~FaceInSurfaceSense`

Checks whether the face normal has the opposite direction (sense) as the underlying surface.
Checks whether the face normal has the opposite direction (sense) as the underlying surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FaceInSurfaceSense() As System.Boolean
```

```

Dim instance As IFace2
Dim value As System.Boolean
 
value = instance.FaceInSurfaceSense()
```

```

System.bool FaceInSurfaceSense()
```

```

System.bool FaceInSurfaceSense(); 
```

#### Return Value

True if face normal and surface normal are in the opposite direction, false if they are in same direction

Remarks

Although the name of this method and its results are somewhat contradictory, the results are:

- True if face normal and surface normal are in the opposite direction.
- False if they are in the same direction.

You might need this method because the underlying surface geometry can have an orientation where its normal vector points toward or away from the body material. The normal vector of faces, however, are directed away from the body material.

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)
