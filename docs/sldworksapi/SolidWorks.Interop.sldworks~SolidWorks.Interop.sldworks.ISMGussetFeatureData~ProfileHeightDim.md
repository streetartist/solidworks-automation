# ProfileHeightDim Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim`

Gets or sets the length of the d2 leg of this gusset.
Gets or sets the length of the d2 leg of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileHeightDim As System.Double
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Double
 
instance.ProfileHeightDim = value
 
value = instance.ProfileHeightDim
```

```

System.double ProfileHeightDim {get; set;}
```

```

property System.double ProfileHeightDim {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of d2 leg

Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.md) is set to 1.

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) Remarks.

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::ProfileAngleDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.md)  
[ISMGussetFeatureData::ProfileLengthDim Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.md)  
[ISMGussetFeatureData::FlipDimSides Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.md)
