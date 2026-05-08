# MaterialInside Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~MaterialInside`

Gets or sets whether to flatten the flange profile with material inside of this swept flange feature.
Gets or sets whether to flatten the flange profile with material inside of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialInside As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean
 
instance.MaterialInside = value
 
value = instance.MaterialInside
```

```

System.bool MaterialInside {get; set;}
```

```

property System.bool MaterialInside {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flatten the flange profile with material inside, false to not

Remarks

This property is valid only:

- if [ISweptFlangeFeatureData::FlattenAlongPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.md) is true,

    - and -

- when not creating the swept flange on an existing sheet metal feature.

The flat pattern of the model may fail for either setting of this property, depending on whether self-intersecting geometry occurs with material inside or outside. You should test your model to determine which setting of this property successfully flattens the flange [profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
