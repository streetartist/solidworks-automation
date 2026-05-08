# SimplifyBends Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~SimplifyBends`

Gets or sets whether to simplify bends in this Flat-Pattern feature.
Gets or sets whether to simplify bends in this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SimplifyBends As System.Boolean
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean
 
instance.SimplifyBends = value
 
value = instance.SimplifyBends
```

```

System.bool SimplifyBends {get; set;}
```

```

property System.bool SimplifyBends {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to simplify edges to lines, false to leave edges complex

Remarks

This property corresponds to the Simplify bends check box on the Parameters group box on the Flat Pattern PropertyManager, which is displayed when you edit the definition of a flat-pattern feature with complex bends in SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)
