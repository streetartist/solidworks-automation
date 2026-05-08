# SetEquationAndConfigurationOption Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption`

Modifies the equation at the specified index for the specified configurations.
Modifies the equation at the specified index for the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEquationAndConfigurationOption( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim WhichConfigurations As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Integer
 
value = instance.SetEquationAndConfigurationOption(Index, Equation, WhichConfigurations, ConfigNames)
```

```

System.int SetEquationAndConfigurationOption( 
   System.int Index,
   System.string Equation,
   System.int WhichConfigurations,
   System.object ConfigNames
)
```

```

System.int SetEquationAndConfigurationOption( 
   System.int Index,
   System.String^ Equation,
   System.int WhichConfigurations,
   System.Object^ ConfigNames
) 
```

#### Parameters

*Index*
:   0-based index of the equation to modify

*Equation*
:   String containing the modified equation (see **Remarks**)

*WhichConfigurations*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigNames*
:   Array of the names of the configurations to which to add this equation; valid only if WhichConfigurations is set to swInConfigurationOpts\_e.swSpecifyConfiguration, in which case, include the name of the current configuration in this array

#### Return Value

Index of equation if successfully modified, -1 if error

Remarks

This method modifies only equations added using [IEquationMgr::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md).

To add an equation using the SOLIDWORKS user interface, you must embed the names of dimensions and global variables in double quotes:

- Global variable assignment:  
  **"B" = 2**
- Component equation:  
  **"N\_SPOKES@CirPattern" = "BARLENGTH@Sketch2" /10**
- Dimension equation that uses the Visual Basic IIf function:  
  **"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5**
- Dimension equation that sets a dimension to the current value:  
  **"D1@Extrude2" =**
- Dimension equation that modifies the right-hand side of an already existing dimension equation:  
  **"D1@Extrude2" = 0.05**

**NOTES:**

- To modify an equation:

  - you must specify Equation with the names of dimensions and global variables in double double quotes and the entire equation in double quotes. The examples for [IEquationMgr::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md) show how to do this.[Global variables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md) cannot be set to current values using this method.
  - added directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md) before calling this method.
- If you change the active configuration, then you must call [IModelDoc2::GetEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEquationMgr.md) again.
- If the model has just one configuration, then use [IEquationMgr::Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md).

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
[IEquationMgr::GetConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.md)  
[IEquationMgr::ISetEquationAndConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ISetEquationAndConfigurationOption.md)  
[IEquationMgr::IAdd3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~IAdd3.md)
