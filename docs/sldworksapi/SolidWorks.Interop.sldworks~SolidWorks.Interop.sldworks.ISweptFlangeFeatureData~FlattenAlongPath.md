# FlattenAlongPath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath`

Gets or sets whether to flatten the flange profile along the sweep path of this swept flange feature.
Gets or sets whether to flatten the flange profile along the sweep path of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlattenAlongPath As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean
 
instance.FlattenAlongPath = value
 
value = instance.FlattenAlongPath
```

```

System.bool FlattenAlongPath {get; set;}
```

```

property System.bool FlattenAlongPath {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flatten the profile along the sweep path, false to not

Remarks

This property is valid only when not creating the swept flange on an existing sheet metal feature.

If this property is true, then you can also specify [ISweptFlangeFeatureData::MaterialInside](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~MaterialInside.md).

If this property is:

- True, then when the model is flattened the [profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Profile.md) flattens and is rotated parallel to the plane of the path. The [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.md) is not flattened, and the result is a the shape of the path.
- False, then when the model is flattened the profile flattens and is rotated perpendicular to the plane of the path. The path is flattened, and the result is a rectangular shape.

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
