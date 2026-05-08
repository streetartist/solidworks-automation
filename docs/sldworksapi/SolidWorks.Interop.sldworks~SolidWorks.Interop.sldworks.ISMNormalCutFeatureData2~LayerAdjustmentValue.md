# LayerAdjustmentValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LayerAdjustmentValue`

Gets or sets the offset plane adjustment value.
Gets or sets the offset plane adjustment value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LayerAdjustmentValue As System.Double
```

```

Dim instance As ISMNormalCutFeatureData2
Dim value As System.Double
 
instance.LayerAdjustmentValue = value
 
value = instance.LayerAdjustmentValue
```

```

System.double LayerAdjustmentValue {get; set;}
```

```

property System.double LayerAdjustmentValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= offset <= 1.0

Remarks

This property is valid only if [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.md) is set to [swNormalCutParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane.

If [ISMNormalCutFeatureData2::LinkToKFactor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LinkToKFactor.md) is set to true, this property is automatically set to 0.5.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
