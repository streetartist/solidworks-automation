# SketchConstraintsDel Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchConstraintsDel`

Obsolete. Superseded by IModelDoc2::SketchConstraintsDel.
Obsolete. Superseded by [IModelDoc2::SketchConstraintsDel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchConstraintsDel( _
   ByVal ConstrInd As System.Integer, _
   ByVal IdStr As System.String _
) 
```

```

Dim instance As IModelDoc
Dim ConstrInd As System.Integer
Dim IdStr As System.String
 
instance.SketchConstraintsDel(ConstrInd, IdStr)
```

```

void SketchConstraintsDel( 
   System.int ConstrInd,
   System.string IdStr
)
```

```

void SketchConstraintsDel( 
   System.int ConstrInd,
   System.String^ IdStr
) 
```

#### Parameters

*ConstrInd*

*IdStr*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
