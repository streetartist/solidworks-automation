# AngularEquationUnits Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AngularEquationUnits`

Gets or sets the angular units used in equations.
Gets or sets the angular units used in equations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AngularEquationUnits As System.Integer
```

```

Dim instance As IEquationMgr
Dim value As System.Integer
 
instance.AngularEquationUnits = value
 
value = instance.AngularEquationUnits
```

```

System.int AngularEquationUnits {get; set;}
```

```

property System.int AngularEquationUnits {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Angular units used in equations as defined in [swAngularEquationUnits\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngularEquationUnits_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
