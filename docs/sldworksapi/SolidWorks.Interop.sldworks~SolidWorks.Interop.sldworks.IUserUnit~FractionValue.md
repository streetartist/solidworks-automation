# FractionValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~FractionValue`

Gets the denominator value of the fraction.
Gets the denominator value of the fraction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FractionValue As System.Integer
```

```

Dim instance As IUserUnit
Dim value As System.Integer
 
instance.FractionValue = value
 
value = instance.FractionValue
```

```

System.int FractionValue {get; set;}
```

```

property System.int FractionValue {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fraction denominator value; valid only if [IUserUnit::FractionBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~FractionBase.md) is [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html).swFRACTION

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
