# Sketch3DIntersections Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Sketch3DIntersections`

Creates new sketch segments based on the selected surfaces.
Creates new sketch segments based on the selected surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Sketch3DIntersections() 
```

```

Dim instance As IModelDoc2
 
instance.Sketch3DIntersections()
```

```

void Sketch3DIntersections()
```

```

void Sketch3DIntersections(); 
```

Remarks

The new sketch segments are added either to the active sketch or to an appropriate new sketch.

If the active sketch is a 2D sketch and the intersection curves are not in that plane, then the resulting sketch segments are projected onto the plane of the sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurface::GetIntersectCurveCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.md)  
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.md)  
[ISurface::IntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve2.md)
