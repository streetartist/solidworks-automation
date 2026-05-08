# AsymmetricFillet Property (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AsymmetricFillet`

Gets or sets whether this variable radius fillet is asymmetric.
Gets or sets whether this variable radius fillet is asymmetric.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AsymmetricFillet As System.Boolean
```

```

Dim instance As IVariableFilletFeatureData2
Dim value As System.Boolean
 
instance.AsymmetricFillet = value
 
value = instance.AsymmetricFillet
```

```

System.bool AsymmetricFillet {get; set;}
```

```

property System.bool AsymmetricFillet {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if an asymmetric fillet, false if a symmetric fillet

Remarks

See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)
