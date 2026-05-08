# Path Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path`

Gets or sets the sweep path of this swept flange feature.
Gets or sets the sweep path of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Path As System.Object
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Object
 
instance.Path = value
 
value = instance.Path
```

```

System.object Path {get; set;}
```

```

property System.Object^ Path {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s or a [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) of lines and arcs

Remarks

If the sweep path is a closed loop, then [ISweptFlangeFeatureData::StartOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~StartOffset.md) and [ISweptFlangeFeatureData::EndOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~EndOffset.md) are not valid.

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) and [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)  
[ISweptFlangeFeatureData::GetPathType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetPathType.md)  
[ISweptFlangeFeatureData::CylindricalOrConicalEdge Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~CylindricalOrConicalEdge.md)  
[ISweptFlangeFeatureData::FlattenAlongPath Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlattenAlongPath.md)
