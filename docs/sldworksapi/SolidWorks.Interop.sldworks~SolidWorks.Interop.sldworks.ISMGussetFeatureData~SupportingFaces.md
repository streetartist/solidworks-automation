# SupportingFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~SupportingFaces`

Gets or sets the legs of this gusset.
Gets or sets the legs of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SupportingFaces As System.Object
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Object
 
instance.SupportingFaces = value
 
value = instance.SupportingFaces
```

```

System.object SupportingFaces {get; set;}
```

```

property System.Object^ SupportingFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of one or two [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to which this gusset is attached

Remarks

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
[ISMGussetFeatureData::ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferencePoint.md)
