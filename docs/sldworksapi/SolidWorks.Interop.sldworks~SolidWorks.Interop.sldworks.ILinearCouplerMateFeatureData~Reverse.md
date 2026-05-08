# Reverse Property (ILinearCouplerMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~Reverse`

Gets or sets whether to reverse the direction of motion of the second mated component relative to the direction of motion of the first mated component of this linear/linear coupler mate.
Gets or sets whether to reverse the direction of motion of the second mated component relative to the direction of motion of the first mated component of this linear/linear coupler mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Reverse As System.Boolean
```

```

Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Boolean
 
instance.Reverse = value
 
value = instance.Reverse
```

```

System.bool Reverse {get; set;}
```

```

property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of motion, false to not

Example

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md)  
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.md)
