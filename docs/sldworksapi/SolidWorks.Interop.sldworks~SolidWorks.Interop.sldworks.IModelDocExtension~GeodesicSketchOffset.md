# GeodesicSketchOffset Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GeodesicSketchOffset`

Creates a geodesic sketch offset along the curvature of a surface.
Creates a geodesic sketch offset along the curvature of a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GeodesicSketchOffset( _
   ByVal Offset As System.Double, _
   ByVal Reverse As System.Boolean, _
   ByVal MakeConstruct As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Offset As System.Double
Dim Reverse As System.Boolean
Dim MakeConstruct As System.Boolean
Dim value As System.Boolean
 
value = instance.GeodesicSketchOffset(Offset, Reverse, MakeConstruct)
```

```

System.bool GeodesicSketchOffset( 
   System.double Offset,
   System.bool Reverse,
   System.bool MakeConstruct
)
```

```

System.bool GeodesicSketchOffset( 
   System.double Offset,
   System.bool Reverse,
   System.bool MakeConstruct
) 
```

#### Parameters

*Offset*
:   Offset distance

*Reverse*
:   True to reverse the offset direction, false to not

*MakeConstruct*
:   True to make sketch construction geometry after offsetting, false to not

#### Return Value

True if the sketch offset is created, false if not

Remarks

To create a Euclidean sketch offset, use [IModelDocExtension::SketchOffsetOnSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.md).

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for each edge to offset and set Append to true and Mark to 1.

After calling this method, call [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md) to rebuild the model with the 3D sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISketchManager::SketchOffset2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.md)  
[IModelDoc2::SketchOffsetEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.md)  
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)
