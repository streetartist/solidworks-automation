# EndOffset Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~EndOffset`

Gets or sets the end offset of this swept flange feature.
Gets or sets the end offset of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndOffset As System.Double
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Double
 
instance.EndOffset = value
 
value = instance.EndOffset
```

```

System.double EndOffset {get; set;}
```

```

property System.double EndOffset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

End offset

Remarks

This property is valid only if [ISweptFlangeFeatureData::Path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.md) is an open loop.

If you want the swept flange to span the entire edge of the model, set both this property and [ISweptFlangeFeatureData::StartOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~StartOffset.md) to 0.0.

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
