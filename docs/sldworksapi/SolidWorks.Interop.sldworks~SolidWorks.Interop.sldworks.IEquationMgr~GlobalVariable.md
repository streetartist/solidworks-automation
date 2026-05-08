# GlobalVariable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable`

Gets whether the equation at the specified index is a global variable.
Gets whether the equation at the specified index is a global variable.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property GlobalVariable( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.GlobalVariable(Index)
```

```

System.bool GlobalVariable( 
   System.int Index
) {get;}
```

```

property System.bool GlobalVariable {
   System.bool get(System.int Index);
}
```

#### Parameters

*Index*
:   0-based index of the equation

#### Property Value

True if the equation at the specified index is a global variable, false if not

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
[IEquationMgr::GetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Value Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value.md)
