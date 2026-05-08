# EntitiesToMate Property (ISymmetricMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate`

Gets or sets the entities in this symmetry mate.
Gets or sets the entities in this symmetry mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EntitiesToMate As System.Object
```

```

Dim instance As ISymmetricMateFeatureData
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

Array of two similar entities: [vertexes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [axes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), [sketch lines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [planar faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), spheres of equal radii, or cylinders of equal radii

Example

See the [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISymmetricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md)  
[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.md)
