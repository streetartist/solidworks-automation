# FilletInnerCorners Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletInnerCorners`

Gets or sets whether to fillet the inner corners of this gusset.
Gets or sets whether to fillet the inner corners of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FilletInnerCorners As System.Boolean
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Boolean
 
instance.FilletInnerCorners = value
 
value = instance.FilletInnerCorners
```

```

System.bool FilletInnerCorners {get; set;}
```

```

property System.bool FilletInnerCorners {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to fillet the inner corners of this gusset, false to not

Remarks

After setting this property, set [ISMGussetFeatureData::InnerCornerFilletRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~InnerCornerFilletRadius.md).

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::FilletOuterCorners Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletOuterCorners.md)
