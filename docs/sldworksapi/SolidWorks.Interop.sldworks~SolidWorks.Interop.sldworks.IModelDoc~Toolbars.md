# Toolbars Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Toolbars`

Obsolete. Superseded by IModelDoc2::Toolbars.
Obsolete. Superseded by [IModelDoc2::Toolbars](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Toolbars.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Toolbars( _
   ByVal M As System.Boolean, _
   ByVal Vw As System.Boolean, _
   ByVal SkMain As System.Boolean, _
   ByVal Sk As System.Boolean, _
   ByVal Feat As System.Boolean, _
   ByVal Constr As System.Boolean, _
   ByVal Macro As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim M As System.Boolean
Dim Vw As System.Boolean
Dim SkMain As System.Boolean
Dim Sk As System.Boolean
Dim Feat As System.Boolean
Dim Constr As System.Boolean
Dim Macro As System.Boolean
 
instance.Toolbars(M, Vw, SkMain, Sk, Feat, Constr, Macro)
```

```

void Toolbars( 
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

```

void Toolbars( 
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
) 
```

#### Parameters

*M*

*Vw*

*SkMain*

*Sk*

*Feat*

*Constr*

*Macro*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
