# IsCut Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut`

Gets or sets whether to remove the intersection area of the target body.
Gets or sets whether to remove the intersection area of the [target body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsCut As System.Boolean
```

```

Dim instance As IIndentFeatureData
Dim value As System.Boolean
 
instance.IsCut = value
 
value = instance.IsCut
```

```

System.bool IsCut {get; set;}
```

```

property System.bool IsCut {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to remove the intersection area of the target body, false to not

Remarks

If this property is set to true, then there is no [thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Thickness.md), but [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.md) is applied.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)
