# GetEquationMgr Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEquationMgr`

Gets the equation manager.
Gets the equation manager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEquationMgr() As EquationMgr
```

```

Dim instance As IModelDoc2
Dim value As EquationMgr
 
value = instance.GetEquationMgr()
```

```

EquationMgr GetEquationMgr()
```

```

EquationMgr^ GetEquationMgr(); 
```

#### Return Value

[Equation manager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)

Remarks

Use the equation manager to work with the existing equations in a model and modify a specific equation.

The [IEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md) object is associated with the configuration that was active at the time it was acquired. If you change the active configuration while holding an IEquationMgr object reference, release it and reacquire it if it is needed.

Example

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)  
[Automatically Solve Equations in Sequence (C#)](Automatically_Solve_Equations_in_Sequence_Example_CSharp.htm)  
[Automatically Solve Equations in Sequence (VB.NET)](Automatically_Solve_Equations_in_Sequence_Example_VBNET.htm)  
[Automatically Solve Equations in Sequence (VBA)](Automatically_Solve_Equations_in_Sequence_Example_VB.htm)  
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)  
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)  
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
