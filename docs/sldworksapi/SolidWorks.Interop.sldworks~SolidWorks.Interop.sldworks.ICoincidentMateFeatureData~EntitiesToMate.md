# EntitiesToMate Property (ICoincidentMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this coincident mate.
Gets or sets the entities to mate in this coincident mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As ICoincidentMateFeatureData
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

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Populate the array of this property by using either IModelDocExtension::SelectByID2 or [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) and [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md).

Create coincident mates with the following mate entity combinations:

| Mate entity/Mate entity | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  (arc, circular edge) | [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md),  [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  (cone) | [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  (coordinate system) | [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  (arc, spline, helix) | ISurface,  IFace2  (cylinder) | IFace2  (extrusion face, draft is not allowed) | IEdge,  [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md),  [ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md),  [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  (line) | [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  (coordinate system origin) | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) | [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md),  [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md),  [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) | ISurface,  IFace2  (sphere) | ISurface |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **IEdge (arc, circular edge)** | ● | ● |  |  | ● |  |  |  | ● | ● |  |  |
| **ISurface, IFace2 (cone)** | ● | ● Both cones must be of the same half angle |  |  |  |  |  |  |  | ● |  |  |
| **IFeature (coordinate system)** |  |  | ● |  |  |  |  | ● |  |  |  |  |
| **ICurve (arc, spline, helix)** |  |  |  |  |  |  |  |  |  | ● |  |  |
| **ISurface, IFace2 (cylinder)** | ● |  |  |  |  |  | ● |  |  |  |  |  |
| **IFace2 (extrusion face, draft is not allowed)** |  |  |  |  |  |  |  |  |  | ● |  |  |
| **IEdge, IRefAxis, ICenterLine, ISketchLine (line)** |  |  |  |  | ● |  | ● |  | ● | ● |  |  |
| **IEntity (coordinate system origin)** |  |  | ● |  |  |  |  | ● |  |  |  |  |
| **IRefPlane** | ● |  |  |  |  |  | ● |  | ● | ● |  |  |
| **IRefPoint, IVertex, ISketchPoint** | ● | ● |  | ● | ● | ● | ● |  | ● | ● | ● | ● |
| **ISurface, IFace2 (sphere)** |  |  |  |  |  |  |  |  |  | ● |  |  |
| **ISurface** |  |  |  |  |  |  |  |  |  | ● |  |  |

After specifying the entities to mate, specify their [ICoincidentMateFeatureData::PickPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~PickPoints.md) to fully define the position of the mate.

Example

See the [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoincidentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md)  
[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.md)
