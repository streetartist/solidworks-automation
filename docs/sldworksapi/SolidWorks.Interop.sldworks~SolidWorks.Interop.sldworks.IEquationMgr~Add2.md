# Add2 Method (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2`

Adds an equation at the specified index.
Adds an equation at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Add2( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String, _
   ByVal Solve As System.Boolean _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim Solve As System.Boolean
Dim value As System.Integer
 
value = instance.Add2(Index, Equation, Solve)
```

```

System.int Add2( 
   System.int Index,
   System.string Equation,
   System.bool Solve
)
```

```

System.int Add2( 
   System.int Index,
   System.String^ Equation,
   System.bool Solve
) 
```

#### Parameters

*Index*
:   0-based index of the new equation (-1 places it at the end of the list)

*Equation*
:   String containing the equation (see **Remarks**)

*Solve*
:   True to solve the equation immediately; false otherwise (see **Remarks**)

#### Return Value

Index of the new equation if successfully added, -1 if an error

Remarks

To add an equation using the SOLIDWORKS user interface, you must embed the names of dimensions and global variables in double quotes:

- Global variable assignment:  
  **"B" = 2**
- Component equation:  
  **"N\_SPOKES@CirPattern" = "BARLENGTH@Sketch2" /10**
- Dimension equation that uses the Visual Basic IIf function:  
  **"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5**
- Dimension equation that sets a dimension to the current value:  
  **"D1@Extrude2" =**

**NOTE:** To add an equation using this method, you must specify Equation with the names of dimensions and global variables in double double quotes and the entire equation in double quotes. See the **Examples**.

If you call this method to add an equation whose left-hand side already exists in another equation, this method returns an error.

Setting the Solve argument to false delays evaluation of this equation, which enhances performance when there are many equations to solve. When Solve is set to false, the equation appears in the FeatureManager design tree only after calling [IEquationaMgr::EvaluateAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.md) or [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

To add equations to models having multiple configurations created in SOLIDWORKS 2014 or later, use [IEquationMgr::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md) instead of this method.

When you add an equation, you are adding it to the list of relations. Thus, do not add an equation while traversing the equations in a model, because SOLIDWORKS could crash.

Example

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)  
[Add Equation and Evaluate All (VB.NET)](Add_Equation_And_Evaluate_All_Example_VBNET.htm)  
[Add Equation and Evaluate All (VBA)](Add_Equation_And_Evaluate_All_Example_VB.htm)  
[Add Equation and Evaluate All (C#)](Add_Equation_And_Evaluate_All_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)  
[IEquationMgr::GetDisabledEquationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md)  
[IEquationMgr::Disabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.md)
