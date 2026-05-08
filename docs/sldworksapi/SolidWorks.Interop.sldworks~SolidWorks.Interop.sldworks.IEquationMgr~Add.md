# Add Method (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add`

Obsolete. Superseded by IEquationMgr::Add2.
Obsolete. Superseded by [IEquationMgr::Add2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Add( _
   ByVal Index As System.Integer, _
   ByVal Equation As System.String _
) As System.Integer
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim Equation As System.String
Dim value As System.Integer
 
value = instance.Add(Index, Equation)
```

```

System.int Add( 
   System.int Index,
   System.string Equation
)
```

```

System.int Add( 
   System.int Index,
   System.String^ Equation
) 
```

#### Parameters

*Index*
:   Index of the new equation (-1 places it at the end of the list)

*Equation*
:   String containing the equation

#### Return Value

Index of the equation; -1 if there was an error

Remarks

The string specified for the equation argument must be formatted as if entered in the SOLIDWORKS user interface (that is, you must embed the names of the dimensions in double quotes). For example:

"N\_SPOKES@CirPattern1" = "BARLENGTH@Sketch2" /10

You can also use the Visual Basic IIf function when specifying a model dimension in the equation argument. For example:

"D1@Extrude2" = (IIf("D1@Extrude3">20, 15, 6))+5

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md)  
[IEquationMgr::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md)  
[IEquationMgr::Equation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md)  
[IEquationMgr::Status Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md)
