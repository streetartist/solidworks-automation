# ShaftFit Property (IStraightElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~ShaftFit`

Gets or sets the shaft fit for this straight hole element.
Gets or sets the shaft fit for this straight hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShaftFit As System.String
```

```

Dim instance As IStraightElementData
Dim value As System.String
 
instance.ShaftFit = value
 
value = instance.ShaftFit
```

```

System.string ShaftFit {get; set;}
```

```

property System.String^ ShaftFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Shaft fit (see **Remarks**)

Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.md) is set to [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard\*DowelHoles.

Set this property to one of the following:

c8, c9, c11, d8, d9, d10, d11, e7, e8, e9, f6, f7, f8, g4, g5, g6, g7, h5, h6, h7, h8, h9, h10, h11, h12, h13, j5, j6, j7, j8, j9, j10, j11, k5, k6, k7, k8, k9, k10, k11, m5, m6, m7, n5, n6, n7, p5, p6, p7, r5, r6, r7, s5, s6, s7, t5, t6, t7, u5, u6, u7, v5, v6, v7, x5, x6, x7

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)  
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.md)
