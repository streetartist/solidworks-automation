# DefaultRadius Property (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius`

Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet.
Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefaultRadius As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim value As System.Double
 
instance.DefaultRadius = value
 
value = instance.DefaultRadius
```

```

System.double DefaultRadius {get; set;}
```

```

property System.double DefaultRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Default radius if a symmetric fillet; default Distance 1 radius if an asymmetric fillet

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetRadius2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md)  
[IVariableFilletFeatureData2::ISetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.md)  
[IVariableFilletFeatureData2::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md)  
[IVariableFilletFeatureData2::DefaultConicRhoOrRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultConicRhoOrRadius.md)  
[IVariableFilletFeatureData2::DefaultDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultDistance.md)
