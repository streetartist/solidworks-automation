# UseBeltThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~UseBeltThickness`

Gets and sets whether to specify belt thickness.
Gets and sets whether to specify belt thickness.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseBeltThickness As System.Boolean
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Boolean
 
instance.UseBeltThickness = value
 
value = instance.UseBeltThickness
```

```

System.bool UseBeltThickness {get; set;}
```

```

property System.bool UseBeltThickness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to specify belt thickness, false to not

Remarks

If this property is true, use [IBeltChainFeatureData::BeltThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltThickness.md) to specify belt thickness.

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
