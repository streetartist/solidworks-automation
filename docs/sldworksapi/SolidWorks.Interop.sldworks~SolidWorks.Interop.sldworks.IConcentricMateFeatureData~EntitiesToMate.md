# EntitiesToMate Property (IConcentricMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this concentric mate.
Gets or sets the entities to mate in this concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As IConcentricMateFeatureData
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

You can create concentric mates with the following mate entity combinations:

| Mate entity/Mate entity | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  (arc, circular edge) | [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md),  (cone) | IRefAxis,  (cylinder) | IEdge,  IRefAxis,  [ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md),  [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  (line) | [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md),  [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md),  [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) | IRefAxis,  ISketchPoint,  IRefPoint,  IVertex  (sphere) |
| --- | --- | --- | --- | --- | --- | --- |
| **IEdge (arc, circular edge)** | ● | ● | ● | ● |  |  |
| **IRefAxis (cone)** | ● | ● | ● | ● | ● |  |
| **IRefAxis (cylinder)** | ● | ● | ● | ● | ● | ● |
| **IEdge, IRefAxis, ICenterLine, ISketchLine (line)** | ● | ● | ● |  |  | ● |
| **IRefPoint, IVertex, ISketchPoint** |  | ● | ● |  |  | ● |
| **IRefAxis, IRefPoint, ISketchPoint, IVertex (sphere)** |  |  | ● | ● | ● | ● |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md)  
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.md)
