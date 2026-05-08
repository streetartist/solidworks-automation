# D2CapEnd Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2CapEnd`

Gets or sets whether to cap the end of the extruded surface in Direction 2.
Gets or sets whether to cap the end of the extruded surface in Direction 2.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2CapEnd As System.Boolean
```

```

Dim instance As ISurfExtrudeFeatureData
Dim value As System.Boolean
 
instance.D2CapEnd = value
 
value = instance.D2CapEnd
```

```

System.bool D2CapEnd {get; set;}
```

```

property System.bool D2CapEnd {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to cap the end in Direction 2, false to not (see **Remarks**)

Remarks

This property is only available if [ISurfExtrudeFeatureData::BothDirections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~BothDirections.md) = true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::D2DraftAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftAngle.md)  
[ISurfExtrudeFeatureData::D2DraftOn Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOn.md)  
[ISurfExtrudeFeatureData::D2DraftOutward Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D2DraftOutward.md)  
[ISurfExtrudeFeatureData::D1CapEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~D1CapEnd.md)
