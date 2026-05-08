# Delete Method (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete`

Deletes the equation at the specified index.
Deletes the equation at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.Delete(Index)
```

```

System.int Delete( 
   System.int Index
)
```

```

System.int Delete( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of the equation to delete

#### Return Value

0 if the equation is deleted; -1 if there was an error

Remarks

When you delete an equation, you are removing it from the list of relations. Thus, do not delete an equation while traversing the equations in a model, because SOLIDWORKS could crash.

Example

[Add Equation and Evalute All (C#)](Add_Equation_And_Evaluate_All_Example_CSharp.htm)  
[Add Equation and Evalute All (VB.NET)](Add_Equation_And_Evaluate_All_Example_VBNET.htm)  
[Add Equation and Evalute All (VBA)](Add_Equation_And_Evaluate_All_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md)  
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Disabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.md)  
[IEquationMgr::GetDisabledEquationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md)
