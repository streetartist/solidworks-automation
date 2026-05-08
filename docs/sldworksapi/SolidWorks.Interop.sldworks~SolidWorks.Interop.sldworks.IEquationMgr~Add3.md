# Add3 Method (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3`

Adds an equation at the specified index for the specified configurations.
Adds an equation at the specified index for the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Add3( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String, _
   ByVal Solve As System.Boolean, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim Solve As System.Boolean
Dim WhichConfigurations As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Integer
 
value = instance.Add3(Index, Equation, Solve, WhichConfigurations, ConfigNames)
```

```

System.int Add3( 
   System.int Index,
   System.string Equation,
   System.bool Solve,
   System.int WhichConfigurations,
   System.object ConfigNames
)
```

```

System.int Add3( 
   System.int Index,
   System.String^ Equation,
   System.bool Solve,
   System.int WhichConfigurations,
   System.Object^ ConfigNames
) 
```

#### Parameters

*Index*
:   0-based index of the new equation (-1 places it at the end of the list)

*Equation*
:   String containing the equation (see **Remarks**)

*Solve*
:   True to solve the equation immediately; false to solve later (see **Remarks**)

*WhichConfigurations*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)

*ConfigNames*
:   Array of the names of the configurations to which to add this equation; valid only if WhichConfigurations is set to swInConfigurationOpts\_e.swSpecifyConfiguration, in which case, include the name of the current configuration in this array

#### Return Value

Index of the new equation if successfully added, -1 if error

Remarks

This method only works for parts having multiple configurations created in SOLIDWORKS 2014 or later. Use this method to add dimension equations, component equations, or global variable assignments to various configurations of models. If you don't have multiple configurations, then call [IEquationMgr::Add2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md), which does not support configurations and is slightly faster.

To add an equation using the SOLIDWORKS user interface, you must embed the names of dimensions and global variables in double quotes:

- Global variable assignment:  
  **"B" = 2**
- Component equation:  
  **"N\_SPOKES@CirPattern" = "BARLENGTH@Sketch2" /10**
- Dimension equation that uses the Visual Basic IIf function:  
  **"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5**
- Dimension equation that sets a dimension to the current value:  
  **"D1@Extrude2" =**

**NOTE:** To add an equation:

- you must specify Equation with the names of dimensions and global variables in double double quotes and the entire equation in double quotes. See the Examples.
- directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md) before calling this method.

You can add a dimension equation whose left-hand side already exists, but only if the existing equation is suppressed. Adding the equation again unsuppresses it. See [IEquationMgr::ChangeSuppressionForAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.md) and [IEquationMgr::ChangeSuppressionForConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.md).

Setting Solve to false delays evaluation of this equation, which enhances performance when there are many equations to solve. When Solve is set to false, the equation appears in the FeatureManager design tree only after calling [IEquationMgr::EvaluateAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.md) or [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

When adding global variable assignments and component equations, WhichConfigurations must be set to [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html).swAllConfiguration.

If you add a global variable assignment that already exists, this method returns an error.

To modify an equation added by this method, call [IEquationMgr::SetEquationAndConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.md).

When you add an equation, you are adding it to the list of relations. Thus, do not add an equation while traversing the equations in a model, because SOLIDWORKS could crash.

Example

[Add and Modify Equations (VBA)](Add_Equations_Example_VB.htm)  
[Add and Modify Equations (VB.NET)](Add_Equations_Example_VBNET.htm)  
[Add and Modify Equations (C#)](Add_Equations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Delete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Status Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)  
[IEquationMgr::GetConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.md)  
[IEquationMgr::IAdd3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~IAdd3.md)  
[IEquationMgr::ISetEquationAndConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ISetEquationAndConfigurationOption.md)  
[IEquationMgr::Disabled Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.md)  
[IEquationMgr::GetDisabledEquationCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md)  
[IEquationMgr::GlobalVariable Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md)
