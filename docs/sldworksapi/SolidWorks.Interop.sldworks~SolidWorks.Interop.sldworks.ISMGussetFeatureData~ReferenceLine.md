# ReferenceLine Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine`

Gets or sets the orientation reference for this gusset's section plane.
Gets or sets the orientation reference for this gusset's section plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferenceLine As System.Object
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Object
 
instance.ReferenceLine = value
 
value = instance.ReferenceLine
```

```

System.object ReferenceLine {get; set;}
```

```

property System.Object^ ReferenceLine {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Line (e.g., [edge,](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) [co-Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md), or [sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)) that is perpendicular to this gusset's section plane

Remarks

If you do not set this property, the assumed reference line is the bend line adjacent to the entities in [ISMGussetFeatureData::SupportingFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~SupportingFaces.md).

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) Remarks.

Example

See the [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.md)
