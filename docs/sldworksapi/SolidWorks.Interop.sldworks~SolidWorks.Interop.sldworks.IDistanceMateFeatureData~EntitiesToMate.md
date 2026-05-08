# EntitiesToMate Property (IDistanceMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this distance mate.
Gets or sets the entities to mate in this distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As IDistanceMateFeatureData
Dim value As System.Object
 
instance.EntitiesToMate = value
 
value = instance.EntitiesToMate
```

```

System.object EntitiesToMate {get; set;}
```

```

property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of entities to mate (see **Remarks**)

Remarks

You can create distance mates with the following mate entity combinations:

| Mate entity/Mate entity | [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md),  [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  (cone) | [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  (arc, spline, helix) | IRefAxis,  IFace2  (cylinder) | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md),  IRefAxis,  [ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md),  [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  (line) | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md),  IFace2 | [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md),  [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md),  [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) | [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md),  IFace2  (sphere) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **IRefAxis, IFace2 (cone)** | ● Both cones must be of the same half angle |  |  |  |  |  |  |
| **ICurve (arc, spline, helix)** |  |  |  |  |  | ● |  |
| **IRefAxis, IFace2 (cylinder)** |  |  | ● | ● | ● | ● |  |
| **IEdge, IRefAxis, ICenterLine, ISketchLine (line)** |  |  | ● | ● | ● | ● | ● |
| **IRefPlane, IFace2** |  |  | ● | ● | ● | ● | ● |
| **IRefPoint, IVertex, ISketchPoint** |  | ● | ● | ● | ● | ● | ● |
| **ISurface, IFace2 (sphere)** |  |  |  | ● | ● | ● | ● |

Example

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md)  
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.md)
