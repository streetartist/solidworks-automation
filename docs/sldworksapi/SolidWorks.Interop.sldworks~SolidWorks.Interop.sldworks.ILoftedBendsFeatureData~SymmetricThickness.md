# SymmetricThickness Property (ILoftedBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~SymmetricThickness`

Gets or sets whether to symmetrically thicken this bi-directional lofted bends feature.
Gets or sets whether to symmetrically thicken this bi-directional lofted bends feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SymmetricThickness As System.Boolean
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean
 
instance.SymmetricThickness = value
 
value = instance.SymmetricThickness
```

```

System.bool SymmetricThickness {get; set;}
```

```

property System.bool SymmetricThickness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to thicken symmetrically, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)
