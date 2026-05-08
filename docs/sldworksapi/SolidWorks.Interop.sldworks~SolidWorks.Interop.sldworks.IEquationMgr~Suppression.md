# Suppression Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Suppression`

Obsolete as of SOLIDWORKS 2014 and later.
Obsolete as of SOLIDWORKS 2014 and later.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Suppression( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean
 
instance.Suppression(Index) = value
 
value = instance.Suppression(Index)
```

```

System.bool Suppression( 
   System.int Index
) {get; set;}
```

```

property System.bool Suppression {
   System.bool get(System.int Index);
   void set (System.int Index, System.bool value);
}
```

#### Parameters

*Index*
:   0-based index of the equation

#### Property Value

True if the equation is suppressed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)
