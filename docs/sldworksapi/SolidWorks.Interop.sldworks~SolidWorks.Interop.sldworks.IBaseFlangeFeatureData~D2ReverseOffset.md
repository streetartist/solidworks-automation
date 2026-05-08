# D2ReverseOffset Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2ReverseOffset`

Gets or sets whether the offset for Direction 2 is reversed for this base flange feature.
Gets or sets whether the offset for Direction 2 is reversed for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2ReverseOffset As System.Boolean
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean
 
instance.D2ReverseOffset = value
 
value = instance.D2ReverseOffset
```

```

System.bool D2ReverseOffset {get; set;}
```

```

property System.bool D2ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True reverses the offset false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::D1ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1ReverseOffset.md)
