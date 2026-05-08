# Status Property (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status`

Gets the status of the last equation that was executed.
Gets the status of the last equation that was executed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Status As System.Integer
```

```

Dim instance As IEquationMgr
Dim value As System.Integer
 
value = instance.Status
```

```

System.int Status {get;}
```

```

property System.int Status {
   System.int get();
}
```

#### Property Value

0-based index of the last equation to successfully execute; -1 if there was an error (see **Remarks**)

Remarks

If you call an IEquationMgr method or property that takes the index of an equation as an argument (e.g., [IEquationMgr::Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value.md)) and call IEquationMgr::Status, then the return value is:

- index of the equation if the call is successful.
- -1 if there is an error.

Example

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
[IEquationMgr::ChangeSuppressionForAllConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.md)  
[IEquationMgr::ChangeSuppressionForConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.md)  
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::EvaluateAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.md)  
[IEquationMgr::Add3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)
