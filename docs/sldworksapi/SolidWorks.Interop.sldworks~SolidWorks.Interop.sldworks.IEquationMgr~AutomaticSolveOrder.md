# AutomaticSolveOrder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticSolveOrder`

Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results.
Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutomaticSolveOrder As System.Boolean
```

```

Dim instance As IEquationMgr
Dim value As System.Boolean
 
instance.AutomaticSolveOrder = value
 
value = instance.AutomaticSolveOrder
```

```

System.bool AutomaticSolveOrder {get; set;}
```

```

property System.bool AutomaticSolveOrder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results and to prevent changing the order in which equations are solved, false to solve equations in the order in which they appear in the equation's Ordered View and to allow changing the order in which equations are solved

Example

[Automatically Solve Equations in Sequence (C#)](Automatically_Solve_Equations_in_Sequence_Example_CSharp.htm)  
[Automatically Solve Equations in Sequence (VB.NET)](Automatically_Solve_Equations_in_Sequence_Example_VBNET.htm)  
[Automatically Solve Equations in Sequence (VBA)](Automatically_Solve_Equations_in_Sequence_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
