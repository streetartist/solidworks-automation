# EntitiesToMate Property (IParallelMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this parallel mate.
Gets or sets the entities to mate in this parallel mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As IParallelMateFeatureData
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

Entities to mate (see **Remarks**)

Remarks

You can create parallel mates with the following mate entity combinations:

| Mate entity/Mate entity | [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)  (cone, cylinder) | IFace2  (extrusion face,  draft is not allowed) | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md),  IRefAxis,  [ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md),  [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  (line) | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) | [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md),  IFace2  (non-analytic  surface) |
| --- | --- | --- | --- | --- | --- |
| **IRefAxis (cone, cylinder)** | ● | ● | ● |  | ● |
| **IFace2 (extrusion face,**  **draft is not allowed)** | ● | ● | ● |  |  |
| **IEdge, IRefAxis, ICenterLine, ISketchLine (line)** | ● | ● | ● | ● | ● |
| **IRefPlane** |  |  | ● | ● |  |
| **ISurface, IFace2**  **(non-analytic surface)** | ● |  | ● |  |  |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [IParallelMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParallelMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.md)  
[IParallelMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData_members.md)
