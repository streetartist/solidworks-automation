# Value Property (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value`

Gets the value of the equation at the specified index.
Gets the value of the equation at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Value( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.Value(Index)
```

```

System.double Value( 
   System.int Index
) {get;}
```

```

property System.double Value {
   System.double get(System.int Index);
}
```

#### Parameters

*Index*
:   0-based index of the equation

#### Property Value

Value or -1 if Index is out of range

Remarks

Example

[Use IIf Function When Adding an Equation (VBA)](Use_IIf_Function_When_Adding_an_Equation_Example_VB.htm)  
[Get Equation Values (C#)](Get_Equation_Values_Example_CSharp.htm)  
[Get Equation Values (VB.NET)](Get_Equation_Values_Example_VBNET.htm)  
[Get Equation Values (VBA)](Get_Equation_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::GlobalVariable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md)
