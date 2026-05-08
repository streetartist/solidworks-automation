# IGetMateParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate~IGetMateParams`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetMateParams( _
   ByRef MateType As System.Integer, _
   ByRef AlignFlag As System.Integer, _
   ByRef CanBeFlipped As System.Integer _
) 
```

```

Dim instance As IMate
Dim MateType As System.Integer
Dim AlignFlag As System.Integer
Dim CanBeFlipped As System.Integer
 
instance.IGetMateParams(MateType, AlignFlag, CanBeFlipped)
```

```

void IGetMateParams( 
   out System.int MateType,
   out System.int AlignFlag,
   out System.int CanBeFlipped
)
```

```

void IGetMateParams( 
   [Out] System.int MateType,
   [Out] System.int AlignFlag,
   [Out] System.int CanBeFlipped
) 
```

#### Parameters

*MateType*

*AlignFlag*

*CanBeFlipped*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate.md)  
[IMate Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate_members.md)
