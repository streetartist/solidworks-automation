# ScaleUniform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform`

Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled.
Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleUniform As System.Double
```

```

Dim instance As IScaleFeatureData
Dim value As System.Double
 
instance.ScaleUniform = value
 
value = instance.ScaleUniform
```

```

System.double ScaleUniform {get; set;}
```

```

property System.double ScaleUniform {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value for the uniform scaling factor

Remarks

You can use:

- [IScaleFeatureData::IsUniform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.md) to enable or disable uniform scaling.  
    
  - or -
- [IScaleFeatureData::GetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.md) or [IScaleFeatureData::SetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.md) to get or set all of the scaling-related values, including uniform scaling, in the same call.

NOTE: If uniform scaling is disabled, then use these properties to get or set the individual scaling values:

- [IScaleFeatureData::ScaleX](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX.md)
- [IScaleFeatureData::ScaleY](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.md)
- [IScaleFeatureData::ScaleZ](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.md)

Example

See [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)
