# AngleSelection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection`

Gets or sets whether to specify angle limits.
Gets or sets whether to specify angle limits.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AngleSelection As System.Boolean
```

```

Dim instance As IHingeMateFeatureData
Dim value As System.Boolean
 
instance.AngleSelection = value
 
value = instance.AngleSelection
```

```

System.bool AngleSelection {get; set;}
```

```

property System.bool AngleSelection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to specify angle limits, false to not

Remarks

After setting this property to true, also set:

- [IHingeMateFeatureData::Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~Angle.md)
- [IHingeMateFeatureData::MaxVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MaxVal.md)
- [IHingeMateFeatureData::MinVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MinVal.md)

Example

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md)  
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.md)
