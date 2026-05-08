# Axis Property (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis`

Gets or sets the entity used to determine the direction of this circular pattern feature.
Gets or sets the entity used to determine the direction of this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Axis As System.Object
```

```

Dim instance As ICircularPatternFeatureData
Dim value As System.Object
 
instance.Axis = value
 
value = instance.Axis
```

```

System.object Axis {get; set;}
```

```

property System.Object^ Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Direction entity (see **Remarks**)

Remarks

This property returns Nothing or null if you do not call [ICircularPatternFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.md) before using this property.

If [ICircularPatternFeatureData::GetAxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetAxisType.md) returns reference axis, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to get [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::VarySketch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~VarySketch.md)
