# AlongCurveOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~AlongCurveOption`

Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points.
Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlongCurveOption As System.Integer
```

```

Dim instance As IRefPointFeatureData
Dim value As System.Integer
 
instance.AlongCurveOption = value
 
value = instance.AlongCurveOption
```

```

System.int AlongCurveOption {get; set;}
```

```

property System.int AlongCurveOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

True enables this option, false does not

Example

See [IRefPointFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md) examples.

Example

[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md)  
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.md)
