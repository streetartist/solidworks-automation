# ChangeSuppressionForAllConfigurations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations`

Changes the suppression state of the specified equation in all configurations.
Changes the suppression state of the specified equation in all configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeSuppressionForAllConfigurations( _
   ByVal Index As System.Integer, _
   ByVal State As System.Boolean _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim State As System.Boolean
Dim value As System.Integer
 
value = instance.ChangeSuppressionForAllConfigurations(Index, State)
```

```

System.int ChangeSuppressionForAllConfigurations( 
   System.int Index,
   System.bool State
)
```

```

System.int ChangeSuppressionForAllConfigurations( 
   System.int Index,
   System.bool State
) 
```

#### Parameters

*Index*
:   0-based index of the target equation

*State*
:   True suppresses the equation, false unsuppresses it

#### Return Value

Index of the equation; -1 if error or if the equation was created in SOLIDWORKS 2014 or later

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::ChangeSuppressionForConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
