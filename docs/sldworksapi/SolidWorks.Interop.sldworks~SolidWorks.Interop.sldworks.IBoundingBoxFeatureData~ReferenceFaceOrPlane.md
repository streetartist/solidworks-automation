# ReferenceFaceOrPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane`

Gets or sets how to create the bounding box.
Gets or sets how to create the bounding box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferenceFaceOrPlane As System.Integer
```

```

Dim instance As IBoundingBoxFeatureData
Dim value As System.Integer
 
instance.ReferenceFaceOrPlane = value
 
value = instance.ReferenceFaceOrPlane
```

```

System.int ReferenceFaceOrPlane {get; set;}
```

```

property System.int ReferenceFaceOrPlane {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fit type as defined in [swGlobalBoundingBoxFitOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html)

Remarks

If this property is set to swGlobalBoundingBoxFitOptions\_e.swBoundingBoxType\_CustomPlane, then select a face or plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with TypeWanted set to [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES before calling this method.

Example

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md)  
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.md)  
[IBoundingBoxFeatureData::PlanarEntity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~PlanarEntity.md)
