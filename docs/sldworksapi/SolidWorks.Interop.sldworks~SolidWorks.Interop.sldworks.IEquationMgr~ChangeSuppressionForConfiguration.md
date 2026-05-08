# ChangeSuppressionForConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration`

Changes the suppression state of an equation in the specified configuration.
Changes the suppression state of an equation in the specified configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeSuppressionForConfiguration( _
   ByVal Index As System.Integer, _
   ByVal ConfigName As System.String, _
   ByVal State As System.Boolean _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim ConfigName As System.String
Dim State As System.Boolean
Dim value As System.Integer
 
value = instance.ChangeSuppressionForConfiguration(Index, ConfigName, State)
```

```

System.int ChangeSuppressionForConfiguration( 
   System.int Index,
   System.string ConfigName,
   System.bool State
)
```

```

System.int ChangeSuppressionForConfiguration( 
   System.int Index,
   System.String^ ConfigName,
   System.bool State
) 
```

#### Parameters

*Index*
:   0-based index of the target equation

*ConfigName*
:   Configuration in which to supress the equation is (Nothing or null for the current configuration)

*State*
:   True suppresses the equation, false unsuppresses it

#### Return Value

Index of the equation; -1 if error of if the equation is created in SOLIDWORKS 2014 or later

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::ChangeSuppressionForAllConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
