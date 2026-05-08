# SketchOffsetOnSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface`

Creates a Euclidean sketch offset from selected edges of a face or surface.
Creates a Euclidean sketch offset from selected edges of a face or surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchOffsetOnSurface( _
   ByVal Offset As System.Double, _
   ByVal Reverse As System.Boolean, _
   ByVal UseFront As System.Boolean, _
   ByVal MakeConstruct As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Offset As System.Double
Dim Reverse As System.Boolean
Dim UseFront As System.Boolean
Dim MakeConstruct As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchOffsetOnSurface(Offset, Reverse, UseFront, MakeConstruct)
```

```

System.bool SketchOffsetOnSurface( 
   System.double Offset,
   System.bool Reverse,
   System.bool UseFront,
   System.bool MakeConstruct
)
```

```

System.bool SketchOffsetOnSurface( 
   System.double Offset,
   System.bool Reverse,
   System.bool UseFront,
   System.bool MakeConstruct
) 
```

#### Parameters

*Offset*
:   Offset distance

*Reverse*
:   True to reverse the 3D sketch, false to not

*UseFront*
:   Although not currently used, must be set to true

*MakeConstruct*
:   True to make the 3D sketch construction geometry after offsetting, false to not

#### Return Value

True if the 3D sketch is created, false if not

Remarks

To create a geodesic sketch offset along the curvature of a surface, use [IModelDocExtension::GeodesicSketchOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GeodesicSketchOffset.md).

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for each edge to offset and set Append to true and Mark to 1.

After calling this method, call [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md) to rebuild the model with the 3D sketch.

Example

[Offset Edges to Create 3D Sketch (C#)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_CSharp.htm)  
[Offset Edges to Create 3D Sketch (VB.NET)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VBNET.htm)  
[Offset Edges to Create 3D Sketch (VBA)](Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISketchManager::SketchOffset2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.md)  
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.md)  
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)
