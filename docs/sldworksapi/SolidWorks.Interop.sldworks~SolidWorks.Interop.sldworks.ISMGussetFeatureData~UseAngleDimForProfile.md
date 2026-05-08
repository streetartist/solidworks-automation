# UseAngleDimForProfile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile`

Gets or sets whether to dimension this gusset using an angle.
Gets or sets whether to dimension this gusset using an angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseAngleDimForProfile As System.Boolean
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Boolean
 
instance.UseAngleDimForProfile = value
 
value = instance.UseAngleDimForProfile
```

```

System.bool UseAngleDimForProfile {get; set;}
```

```

property System.bool UseAngleDimForProfile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use an angle to dimension this gusset, false to not

Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.md) is set to 1.

After setting this property to true, set [ISMGussetFeatureData::ProfileAngleDim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.md).

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) Remarks.

Example

See the [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)
