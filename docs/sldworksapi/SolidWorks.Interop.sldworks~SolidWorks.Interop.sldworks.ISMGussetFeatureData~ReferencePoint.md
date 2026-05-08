# ReferencePoint Property (ISMGussetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint`

Gets or sets a position reference for this gusset.
Gets or sets a position reference for this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePoint As System.Object
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Object
 
instance.ReferencePoint = value
 
value = instance.ReferencePoint
```

```

System.object ReferencePoint {get; set;}
```

```

property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Point (e.g., [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), or [reference point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md)) where to position this gusset

Remarks

If you do not set this property, you must set [ISMGussetFeatureData::UseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseOffset.md) and [ISMGussetFeatureData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.md) to offset the gusset from an assumed reference point. For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) Remarks.

Example

See the [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::ReferenceLine Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.md)  
[ISMGussetFeatureData::SupportingFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~SupportingFaces.md)
