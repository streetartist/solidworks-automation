# HoleFit Property (IStraightElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~HoleFit`

Gets or sets the hole fit for this straight hole element.
Gets or sets the hole fit for this straight hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HoleFit As System.String
```

```

Dim instance As IStraightElementData
Dim value As System.String
 
instance.HoleFit = value
 
value = instance.HoleFit
```

```

System.string HoleFit {get; set;}
```

```

property System.String^ HoleFit {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Hole fit (see **Remarks**)

Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.md) is set to [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard\*DowelHoles.

Set this property to one of the following:

C8, C9, C11, D8, D9, D10, D11, E7, E8, E9, F6, F7, F8, F9, G5, G6, G7, G8, G9, G10, H5, H6, H7, H8, H9, H10, H11, H12, H13, J6, J7, J8, J9, J10, J11, K6, K7, K8, M6, M7, M8, N6, N7, N8, N9, N10, N11, P6, P7, R7, S6, S7, T6, T7, U6, U7, V6, V7, X6, X7

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)  
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.md)
