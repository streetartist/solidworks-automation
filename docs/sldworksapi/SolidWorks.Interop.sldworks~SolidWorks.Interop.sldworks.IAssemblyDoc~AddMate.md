# AddMate Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate`

Obsolete. Superseded by IAssemblyDoc::AddMate3.
Obsolete. Superseded by [IAssemblyDoc::AddMate3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AddMate( _
   ByVal MateType As System.Integer, _
   ByVal Align As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Dist As System.Double, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IAssemblyDoc
Dim MateType As System.Integer
Dim Align As System.Integer
Dim Flip As System.Boolean
Dim Dist As System.Double
Dim Angle As System.Double
 
instance.AddMate(MateType, Align, Flip, Dist, Angle)
```

```

void AddMate( 
   System.int MateType,
   System.int Align,
   System.bool Flip,
   System.double Dist,
   System.double Angle
)
```

```

void AddMate( 
   System.int MateType,
   System.int Align,
   System.bool Flip,
   System.double Dist,
   System.double Angle
) 
```

#### Parameters

*MateType*

*Align*

*Flip*

*Dist*

*Angle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
