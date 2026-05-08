# ISetEquationAndConfigurationOption Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ISetEquationAndConfigurationOption`

Modifies the equation at the specified index for the specified configurations.
Modifies the equation at the specified index for the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetEquationAndConfigurationOption( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal ConfigCount As System.Integer, _
   ByRef ConfigNames As System.String _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim WhichConfigurations As System.Integer
Dim ConfigCount As System.Integer
Dim ConfigNames As System.String
Dim value As System.Integer
 
value = instance.ISetEquationAndConfigurationOption(Index, Equation, WhichConfigurations, ConfigCount, ConfigNames)
```

```

System.int ISetEquationAndConfigurationOption( 
   System.int Index,
   System.string Equation,
   System.int WhichConfigurations,
   System.int ConfigCount,
   ref System.string ConfigNames
)
```

```

System.int ISetEquationAndConfigurationOption( 
   System.int Index,
   System.String^ Equation,
   System.int WhichConfigurations,
   System.int ConfigCount,
   System.String^% ConfigNames
) 
```

#### Parameters

*Index*
:   0-based index of the equation to modify

*Equation*
:   String containing the modified equation (see **Remarks**)

*WhichConfigurations*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigCount*
:   Number of names in ConfigNames array

*ConfigNames*
:   - in-process, in-process, unmanaged C++: Pointer to an array of strings containing configuration names

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

0 if equation successfully added, -1 if error

Remarks

This method modifies only equations added using [IEquationMgr::IAdd3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~IAdd3.md).

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

  - you must specify Equation with the names of dimensions and global variables in double double quotes and the entire equation in double quotes. The examples for [IEquationMgr::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md) show how to do this. [Global variables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md) cannot be set to current values using this method.
  - added directly to an assembly component's model, you must call [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md) before calling this method.
- If you change the active configuration, then you must call [IModelDoc2::GetEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEquationMgr.md) again.
- If the model has just one configuration, then use [IEquationMgr::Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::SetEquationAndConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.md)  
[IEquationMgr::GetConfigurationOption Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.md)
