# LinkToKFactor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LinkToKFactor`

Gets or sets whether to link to a K-Factor when adjusting the offset plane of this Normal Cut.
Gets or sets whether to link to a K-Factor when adjusting the offset plane of this Normal Cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToKFactor As System.Boolean
```

```

Dim instance As ISMNormalCutFeatureData2
Dim value As System.Boolean
 
instance.LinkToKFactor = value
 
value = instance.LinkToKFactor
```

```

System.bool LinkToKFactor {get; set;}
```

```

property System.bool LinkToKFactor {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link to a K-Factor, false to not

Remarks

This property is valid only if:

- [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.md) is set to [swNormalCutParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane

    - and -

- [ISMNormalCutFeatureData2::OffsetPlaneReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OffsetPlaneReference.md) is set.

If this property is set to true, then [ISMNormalCutFeatureData2::LayerAdjustmentValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LayerAdjustmentValue.md) is automatically set to 0.5.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
