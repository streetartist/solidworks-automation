# EntitiesToMate Property (ITangentMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData~EntitiesToMate`

Gets or sets the entities to mate in this tangent mate.
Gets or sets the entities to mate in this tangent mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As ITangentMateFeatureData
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

You can create tangent mates with the following mate entity combinations:

| Mate entity/Mate entity | [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md),  [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  (cone, cylinder) | IFace2  (extrusion face, draft is not allowed) | [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md),  IRefAxis,  [ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md),  [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  (line) | [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) | ISurface,  IFace2  (sphere) | ISurface |
| --- | --- | --- | --- | --- | --- | --- |
| **ISurface, IFace2 (cone, cylinder)** | ● | ● | ● | ● | ● | ● |
| **IFace2 (extrusion face; draft is not allowed)** | ● |  |  |  | ● |  |
| **IEdge, IRefAxis, ICenterLine, ISketchLine (line)** | ● |  |  |  | ● |  |
| **IRefPlane** | ● |  |  |  | ● |  |
| **ISurface, IFace2 (sphere)** | ● | ● | ● | ● | ● | ● |
| **ISurface** | ● |  |  |  | ● |  |

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Example

See the [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITangentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.md)  
[ITangentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData_members.md)
