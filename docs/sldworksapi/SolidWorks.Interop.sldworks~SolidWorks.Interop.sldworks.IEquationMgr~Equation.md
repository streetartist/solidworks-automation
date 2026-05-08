# Equation Property (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation`

Gets or sets the equation at the specified index.
Gets or sets the equation at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Equation( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.String
 
instance.Equation(Index) = value
 
value = instance.Equation(Index)
```

```

System.string Equation( 
   System.int Index
) {get; set;}
```

```

property System.String^ Equation {
   System.String^ get(System.int Index);
   void set (System.int Index, System.String^ value);
}
```

#### Parameters

*Index*
:   0-based index of the equation

#### Property Value

String containing the equation

Remarks

The string set by this property must be formatted as if entered in the SOLIDWORKS user interface; that is, you must embed the names of the dimensions and global variables in double double quotes. To use the following examples to specify Equation, you must replace every double quote with double double quotes, and enclose the entire equation with double quotes.

      Global variable assignment:

> **"B" = 2**

      Component equation:

> "**N\_SPOKES@CirPattern1" = "BARLENGTH@Sketch2" /10**

      Dimension equation that uses the Visual Basic IIf function:

> **"D1@Extrude2" = (("D1@Extrude3">20, 15, 6))+5**

      Dimension equation that sets a dimension to the current value:

> **"D1@Extrude2" =**

      Dimension equation that modifies the right-hand side of an already existing dimension equation:

> **"D1@Extrude2" = 0.05**

**NOTE:** To set an equation:

- directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md) before calling this method.
- for specific configurations in a model with multiple configurations, use [IEquationMgr::SetEquationAndConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.md).

Example

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)  
[Disable Equation (C#)](Disable_Equation_Example_CSharp.htm)  
[Disable Equation (VB.NET)](Disable_Equation_Example_VBNET.htm)  
[Disable Equation (VBA)](Disable_Equation_Example_VB.htm)  
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)  
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)  
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md)  
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::EvaluateAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.md)  
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md)  
[IEquationMgr::Disabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.md)  
[IEquationMgr::GetDisabledEquationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md)  
[IEquationMgr::GlobalVariable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md)  
[IEquationMgr::AutomaticSolveOrder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticSolveOrder.md)  
[IEquationMgr::AutomaticRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticRebuild.md)
