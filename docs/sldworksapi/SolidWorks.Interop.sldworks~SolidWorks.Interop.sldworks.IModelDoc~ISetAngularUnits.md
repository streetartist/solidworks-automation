# ISetAngularUnits Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISetAngularUnits`

Obsolete. Superseded by IModelDoc2::ISetAngularUnits.
Obsolete. Superseded by [IModelDoc2::ISetAngularUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetAngularUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short _
) 
```

```

Dim instance As IModelDoc
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short
 
instance.ISetAngularUnits(UType, FractBase, FractDenom, SigDigits)
```

```

void ISetAngularUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

```

void ISetAngularUnits( 
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
) 
```

#### Parameters

*UType*

*FractBase*

*FractDenom*

*SigDigits*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
