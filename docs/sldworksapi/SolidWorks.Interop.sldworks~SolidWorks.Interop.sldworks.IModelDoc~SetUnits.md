# SetUnits Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUnits`

Obsolete. Superseded by IModelDoc2::SetUnits.
Obsolete. Superseded by [IModelDoc2::SetUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short, _
   ByVal RoundToFraction As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short
Dim RoundToFraction As System.Boolean
 
instance.SetUnits(UType, FractBase, FractDenom, SigDigits, RoundToFraction)
```

```

void SetUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
)
```

```

void SetUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
) 
```

#### Parameters

*UType*

*FractBase*

*FractDenom*

*SigDigits*

*RoundToFraction*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
