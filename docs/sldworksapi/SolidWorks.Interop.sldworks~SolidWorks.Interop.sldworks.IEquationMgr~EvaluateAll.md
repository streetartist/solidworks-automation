# EvaluateAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll`

Evaluates all equations.
Evaluates all equations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EvaluateAll() As System.Integer
```

```

Dim instance As IEquationMgr
Dim value As System.Integer
 
value = instance.EvaluateAll()
```

```

System.int EvaluateAll()
```

```

System.int EvaluateAll(); 
```

#### Return Value

-1 for both success and failure

Remarks

Use this method to solve all equations that were added by [IEquationMgr::Add2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md) or [IEquationMgr::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md) where Solve is set to false.

Example

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)  
[Add Equation and Evaluate All (VBA)](Add_Equation_And_Evaluate_All_Example_VB.htm)  
[Add Equation and Evaluate All (VB.NET)](Add_Equation_And_Evaluate_All_Example_VBNET.htm)  
[Add Equation and Evaluate All (C#)](Add_Equation_And_Evaluate_All_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)
