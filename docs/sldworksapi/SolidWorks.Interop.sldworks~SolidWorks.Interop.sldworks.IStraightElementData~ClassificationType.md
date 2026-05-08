# ClassificationType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~ClassificationType`

Gets or sets the classification type of this straight hole element.
Gets or sets the classification type of this straight hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ClassificationType As System.Integer
```

```

Dim instance As IStraightElementData
Dim value As System.Integer
 
instance.ClassificationType = value
 
value = instance.ClassificationType
```

```

System.int ClassificationType {get; set;}
```

```

property System.int ClassificationType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Classification type as defined in [swStraightHoleClassificationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightHoleClassificationType_e.html)

Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.md) is set to [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard\*DowelHoles.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)  
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.md)
