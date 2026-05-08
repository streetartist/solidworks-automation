# AsymmetricFillet Property (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet`

Gets or sets whether this simple fillet/chamfer is asymmetric.
Gets or sets whether this simple fillet/chamfer is asymmetric.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AsymmetricFillet As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
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

True if an asymmetric fillet/chamfer, false if a symmetric fillet/chamfer

Example

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) introductory example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
