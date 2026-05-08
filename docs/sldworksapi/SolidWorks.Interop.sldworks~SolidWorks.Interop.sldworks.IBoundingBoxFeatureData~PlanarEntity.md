# PlanarEntity Property (IBoundingBoxFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~PlanarEntity`

Gets or sets the reference face or plane for this bounding box feature.
Gets or sets the reference face or plane for this bounding box feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PlanarEntity As System.Object
```

```

Dim instance As IBoundingBoxFeatureData
Dim value As System.Object
 
instance.PlanarEntity = value
 
value = instance.PlanarEntity
```

```

System.object PlanarEntity {get; set;}
```

```

property System.Object^ PlanarEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

This property is valid only if [IBoundingBoxFeatureData::ReferenceFaceOrPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane.md) is set to [swGlobalBoundingBoxFitOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html).swBoundingBoxType\_CustomPlane.

Example

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md)  
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.md)
