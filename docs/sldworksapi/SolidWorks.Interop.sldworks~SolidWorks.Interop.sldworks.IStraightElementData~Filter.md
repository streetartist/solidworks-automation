# Filter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~Filter`

Gets or sets the filter for this straight hole element.
Gets or sets the filter for this straight hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Filter As System.Integer
```

```

Dim instance As IStraightElementData
Dim value As System.Integer
 
instance.Filter = value
 
value = instance.Filter
```

```

System.int Filter {get; set;}
```

```

property System.int Filter {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Filter as defined in [swStraightHoleFilter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightHoleFilter_e.html)

Remarks

This property is valid only if [IAdvancedHoleElementData::Standard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Standard.md) is set to [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandards_e.html):

- swStandardPEMInch

    - or -

- swStandardPEMMetric

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)  
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.md)
