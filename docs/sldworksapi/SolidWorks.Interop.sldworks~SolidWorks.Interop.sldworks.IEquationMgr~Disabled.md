# Disabled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled`

Gets or sets whether to disable the specified equation in the model.
Gets or sets whether to disable the specified equation in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Disabled( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean
 
instance.Disabled(Index) = value
 
value = instance.Disabled(Index)
```

```

System.bool Disabled( 
   System.int Index
) {get; set;}
```

```

property System.bool Disabled {
   System.bool get(System.int Index);
   void set (System.int Index, System.bool value);
}
```

#### Parameters

*Index*
:   0-based index of the equation

#### Property Value

True to disable the specified equation, false to not

Remarks

When you disable an equation, you are removing it from the list of relations. Thus, do not disable an equation while traversing the equations in a model, because SOLIDWORKS could crash.

Example

[Disable Equation (C#)](Disable_Equation_Example_CSharp.htm)  
[Disable Equation (VB.NET)](Disable_Equation_Example_VBNET.htm)  
[Disable Equation (VBA)](Disable_Equation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Add2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md)  
[IEquationMgr::Add3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md)  
[IEquationMgr::Delete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::GetDisabledEquationCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)
