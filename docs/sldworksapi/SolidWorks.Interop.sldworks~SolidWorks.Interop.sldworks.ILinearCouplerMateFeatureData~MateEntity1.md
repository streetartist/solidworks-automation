# MateEntity1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity1`

Gets or sets the entity of the first mated component of this linear/linear coupler mate.
Gets or sets the entity of the first mated component of this linear/linear coupler mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MateEntity1 As System.Object
```

```

Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object
 
instance.MateEntity1 = value
 
value = instance.MateEntity1
```

```

System.object MateEntity1 {get; set;}
```

```

property System.Object^ MateEntity1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

First mated component entity ([face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md))

Example

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md)  
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.md)
